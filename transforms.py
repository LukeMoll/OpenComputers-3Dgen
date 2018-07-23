import numpy as n

"""
Homogenous tranformations for 3D coordinates represented in a 4-high column vector (4r, 1c matrix)
"""

def identity():
    return n.array([[ 1, 0, 0, 0],
                    [ 0, 1, 0, 0],
                    [ 0, 0, 1, 0],
                    [ 0, 0, 0, 1]])
            
def translate(x,y,z):
    return n.array([[ 1, 0, 0, x],
                    [ 0, 1, 0, y],
                    [ 0, 0, 1, z],
                    [ 0, 0, 0, 1]])

def reflectX():
    return n.array([[-1, 0, 0, 0],
                    [ 0, 1, 0, 0],
                    [ 0, 0, 1, 0],
                    [ 0, 0, 0, 1]])

def reflectY():
    return n.array([[ 1, 0, 0, 0],
                    [ 0,-1, 0, 0],
                    [ 0, 0, 1, 0],
                    [ 0, 0, 0, 1]])

def reflectZ():
    return n.array([[ 1, 0, 0, 0],
                    [ 0, 1, 0, 0],
                    [ 0, 0,-1, 0],
                    [ 0, 0, 0, 1]])

def swapAxes(func):
    """
        func (x, y, z): takes a tuple and returns it, but with its elements in a different order
    """
    return n.array([list(func((1,0,0))) + [0],
                    list(func((0,1,0))) + [0],
                    list(func((0,0,1))) + [0],
                    [0,0,0,1]])
