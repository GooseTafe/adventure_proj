from Inventory import Inventory
from Characters.BaseCharacter import BaseCharacter


# Gilbert the main character and the player
class Adventurer(BaseCharacter):
    def __init__(self):
        self.name = "gilbert"
        self.description = "Gilbert is a 5 foot 8 human with pinkish skin and a very muscular body"
        self.bag = Inventory()
        self.life = 15
        self.position = (0, 1)
        self.equipment = []
