from Locations.BaseLocation import BaseLocation
from Characters.Adventurer import Adventurer


class House(BaseLocation):
    def __init__(self):
        self.description = "Gilberts house, nothing interesting to speak of as it is just a place to sleep"
        self.character = Adventurer()

    def give_summary(self):
        pass