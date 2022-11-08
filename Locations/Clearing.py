from Locations.BaseLocation import BaseLocation
from Characters.KingBoar import KingBoar


class Clearing(BaseLocation):
    def __init__(self):
        self.character = KingBoar()
        self.description = "a clearing in the forest where light is shining through the trees"

    def give_summary(self):
        pass