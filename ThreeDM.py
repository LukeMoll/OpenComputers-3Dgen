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
        self.startP = startP
        self.endP = endP
        self.texture = texture
        if tint != None: self.tint = tint
        self.onState = onState

    def __str__(self):
        return "{{ {},{},{},{},{},{},texture=\"{}\"{}{}}},".format( self.startP[0], self.startP[1], self.startP[2], self.endP[0], self.endP[1], self.endP[2], self.texture, ",tint={}".format(self.tint) if self.tint != None else "", ",state={}".format(self.onState).lower() if self.onState else "")