from Locations.BaseLocation import BaseLocation
from Characters.Grandpa import Grandpa


# A village where the player meets the info character grandpa
class Village(BaseLocation):
    def __init__(self):
        self.name = "Village"
        self.character = Grandpa()
        self.description = "a quiet village where Gilbert lives"

    def give_summary(self):
        pass