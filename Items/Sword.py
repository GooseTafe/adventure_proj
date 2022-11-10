from BaseItem import BaseItem


class Sword(BaseItem):
    def __init__(self):
        self.name = "sword"
        self.description = "Sword; A sharp iron sword the length of an arm, used for attacking foes"
        self.equip = False
        self.damage = None

