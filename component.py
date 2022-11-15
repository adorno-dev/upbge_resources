from mathutils import Vector

import bge

class CharacterComponent(bge.types.KX_PythonComponent):

    args = {
        "Health": 100,
        "Stamina": 100,
        "Race": {
            "Orc",
            "Elf",
            "Human",
            "Undead"
        },
        "Position": Vector([0,0,0])
    }

    def start(self, args):
        self.health = args["Health"]
        self.stamina = args["Stamina"]
        self.object.worldPosition = args["Position"]
    
    def update(self):
        self.object.applyRotation([0,0,.1], True)
