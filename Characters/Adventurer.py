from Inventory import Inventory
from Characters.BaseCharacter import BaseCharacter


class Adventurer(BaseCharacter):
    def __init__(self):
        self.name = "gilbert"
        self.description = "Gilbert is a 5 foot 8 human with pinkish skin and a very muscular body"
        self.bag = Inventory()
        self.life = 3
        self.position = (0, 1)
        self.equipment = []
