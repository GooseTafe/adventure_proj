from Locations.BaseLocation import BaseLocation
from Characters.Farmer import Farmer


class Village(BaseLocation):
    def __init__(self):
        self.character = Farmer()
        self.description = "a quiet village where Gilbert lives"

    def give_summary(self):
        pass