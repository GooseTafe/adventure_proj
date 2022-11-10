from Locations.BaseLocation import BaseLocation
from Characters.Adventurer import Adventurer
from Items.Sword import Sword


class House(BaseLocation):
    def __init__(self):
        self.description = "Gilbert's house, nothing interesting to speak of as it is just a place to sleep"
        self.character = Adventurer()
        self.item = Sword()

    def give_summary(self):
        pass