import numpy as np

class ThreeDM:
    def __init__(self, name, tooltip="", lightLevel=0, emitRedstone=False,
     buttonMode=False, playerCollidable=True, entityCollidable=True):
        self.name = name
        self.tooltip = tooltip
        self.lightLevel = lightLevel
        self.emitRedstone = emitRedstone
        self.buttonMode = buttonMode
        self.playerCollidable = playerCollidable
        self.entityCollidable = entityCollidable
        self.shapes = []

    def addShape(self,shape):
        self.shapes.append(shape)

    def transform(self, mat):
        """
        Applies Shape.transform(mat) to each of the shapes in this model
        """
        for shape in self.shapes: shape.transform(mat)

    def __str__(self):
        return """
{{
    label="{}",
    tooltip="{}",
    lightLevel={},
    emitRedstone={},
    buttonMode={},
    collidable={{{},{}}},
    shapes={{
        {}
    }},
}}""".format(self.name, self.tooltip, self.lightLevel, 
    str(self.emitRedstone).lower(), str(self.buttonMode).lower(),
    str(self.playerCollidable).lower(), str(self.entityCollidable).lower(),
    "\n".join(list(map(str, self.shapes))))

class Shape:
    def __init__(self, startP, endP, texture, tint=None, onState=False):
        """
        Args:
            startP: 3-tuple (x,y,z) of the starting corner
            endP: as startP for the end corner
            texture: which texture to use

            tint: string in format 0xRRGGBB hex-encoded 00 to FF for R, G, B
            onState: whether this is in the "on" state or not
        """
        self.start = np.array([startP + (1,)]).transpose()
        self.end = np.array([endP + (1,)]).transpose()
        self.texture = texture
        if tint != None: self.tint = tint
        self.onState = onState
    
    def transform(self, mat):
        """
        Transforms this shape using homogenous coordinates.

        Args:
            mat: 4x4 numpy array representing a 4D linear transformation
        """
        self.start = mat @ self.start
        self.end = mat @ self.end

    def __str__(self):
        return "{{ {},{},{},{},{},{},texture=\"{}\"{}{}}},".format( self.start[0][0], self.start[1][0], self.start[2][0], self.end[0][0], self.end[1][0], self.end[2][0], self.texture, ",tint={}".format(self.tint) if self.tint != None else "", ",state={}".format(self.onState).lower() if self.onState else "")