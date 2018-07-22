from flask import Flask
from PIL import Image
import numpy

from blocks import blocks
solidblocks = [b for b in blocks if b[2] < 32 and b[1][3] == 255]

from ThreeDM import ThreeDM, Shape

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def face():
    im = Image.open("steve_head.png")
    shapes = ""
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            pix = im.getpixel((x,y))
            nB = nearestBlock(pix)
            shapes += "{{ {}, {}, 0, {}, {}, 1, texture=\"{}\"}},\n".format(x,8-(y+1),x+1,8-y,nB[0].split("/")[-1].split(".")[0])
    return shapes


@app.route('/hex.3dm')
def hex3dm():
    im = Image.open("steve_head.png")
    model = ThreeDM("Steve head")
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            pix = im.getpixel((x,y))
            model.addShape(Shape((x,8-(y+1),0), (x+1,8-y,1), "iron_block", rgbToHex(pix)))
    return str(model)

@app.route('/face/<username>.3dm')
def face3dm(username):
    skin = fetch_skin(username)
    im = skin.crop((8,8,16,16))
    model = ThreeDM("{}'s face".format(username))
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            pix = im.getpixel((x,y))
            model.addShape(Shape((x,8-(y+1),0), (x+1,8-y,1), "iron_block", rgbToHex(pix)))
    return str(model)

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
    return Image.open("head.png")