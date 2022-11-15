import bge

tap = bge.logic.KX_INPUT_JUST_ACTIVATED
mouse = bge.logic.mouse.inputs
keys = bge.logic.keyboard.inputs

class Character(bge.types.KX_GameObject):

    def __init__(self, _) -> None:
        self.health = 100
        self.stamina = 100
    
    def update(self, controller):
        self.check_keyboard_control()

    def check_keyboard_control(self):
        if keys[bge.events.WKEY].values[-1]:
            self.applyMovement([0,.1,0], True)
        elif keys[bge.events.SKEY].values[-1]:
            self.applyMovement([0,-.1,0], True)

        if keys[bge.events.AKEY].values[-1]:
            self.applyRotation([0,0,.05], True)
        elif keys[bge.events.DKEY].values[-1]:
            self.applyRotation([0,0,-.05], True)

    def damage(self, value):
        self.health -= value
