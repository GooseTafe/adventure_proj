from BaseItem import BaseItem


# used to block attacks
class Shield(BaseItem):
    def __init__(self):
        self.name = "shield"
        self.description = "Shield; a wooden shield, used for defending"
        self.equip = False