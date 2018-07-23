from flask import Flask
from PIL import Image
import numpy

# from blocks import blocks
# solidblocks = [b for b in blocks if b[2] < 32 and b[1][3] == 255]

from ThreeDM import ThreeDM, Shape
from mojang import Mojang
import transforms as tf

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

"""
def textures():
    im = Image.open("steve_head.png")
    shapes = ""
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            pix = im.getpixel((x,y))
            nB = nearestBlock(pix)
            shapes += "{{ {}, {}, 0, {}, {}, 1, texture=\"{}\"}},\n".format(x,8-(y+1),x+1,8-y,nB[0].split("/")[-1].split(".")[0])
    return shapes
"""

@app.route('/face/<username>.3dm')
def face3dm(username):
    skin = fetch_skin(username)
    im = skin.crop((8,8,16,16))
    model = ThreeDM("{}'s face".format(username))
    shapes = imTo3d(im)
    for shape in shapes: model.addShape(shape)
    model.transform(tf.reflectY())
    model.transform(tf.translate(0,8,0))
    model.transform(tf.translate(1,1,0))
    return str(model)


head_flip = tf.translate(0,8,0) @ tf.reflectY()

head_face = tf.translate(1,1,0) @ head_flip
head_back = tf.translate(1,1,9) @ tf.translate(8,0,0) @ tf.reflectX() @ head_flip
head_left = tf.translate(0,1,1) @ tf.translate(0,0,8) @ tf.reflectZ() @ tf.swapAxes(lambda p:(p[2],p[1],p[0]))
head_right = tf.translate(9,0,0) @ head_left
head_bottom = tf.translate(1,0,1) @ tf.swapAxes(lambda p:(p[0],p[2],p[1])) @ head_flip
head_top = tf.translate(0,9,0) @ head_bottom

head_parts = [
    ( (8,8,16,16) , head_face),
    ( (32,8,40,16) , head_back),
    ( (0,8,8,16) , head_left),
    ( (16,8,24,16) , head_right),
    ( (8,0,16,8) , head_top),
    ( (16,0,24,0) , head_bottom)
]

@app.route('/head/<username>.3dm')
def head3dm(username):
    skin = fetch_skin(username)
    model = ThreeDM("{}'s head".format(username))
    
    for part in head_parts:
        im = skin.crop(part[0])
        part_shapes = imTo3d(im)
        for shape in part_shapes: 
            shape.transform(part[1])
            model.addShape(shape)
    
    return str(model)





def imTo3d(im):
    shapes = []
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            pix = im.getpixel((x,y))
            shapes.append(Shape((x,y,0), (x+1,y+1,1), "iron_block", rgbToHex(pix)))
    return shapes

def rgbToHex(c):
    def norm(n): return min(255, max(1, int(n)))
    return "0x{:02x}{:02x}{:02x}".format(norm(c[0]),norm(c[1]),norm(c[2]))

def nearestBlock(pixel):
    return min(solidblocks, key=lambda b: distance(pixel, b[1]))

def distance(c1, c2):
    a1 = numpy.array(c1[:3])
    a2 = numpy.array(c2[:3])
    return numpy.linalg.norm(a1 - a2)

def fetch_skin(username):
    (uuid, uErr) = Mojang.getUUID(username)
    if uErr != None or len(uuid) < 1:
        return Image.open("4px_reference.png")
    else:
        return Mojang.getSkin(uuid[0]['id'])
