from PIL import Image
from sys import argv
import numpy as numpy
import math

def main():
    print("blocks = ",[
        (path,) + averageImage(Image.open(path))
        for path in argv[1:]
    ])

"""

    im: PIL.Image
"""
def averageImage(im):
    im = im.convert(mode="RGBA")
    pairs = [averageChannel(im.getchannel(x)) for x in im.getbands()]
    return tuple(
        [tuple([math.floor(p[0]) for p in pairs]),
        max([math.floor(p[1]) for p in pairs])]
    )

def averageChannel(channel):
    arr = numpy.array(channel).reshape([-1])
    return (numpy.average(arr), numpy.std(arr))


if __name__ == '__main__':
    main()