from character import Character

def start(controller):
    controller.owner["character"] = Character(controller.owner)

def update(controller):
    controller.owner.update(controller)