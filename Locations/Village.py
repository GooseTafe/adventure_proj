from Locations.BaseLocation import BaseLocation
from Characters.Grandpa import Grandpa


class Village(BaseLocation):
    def __init__(self):
        self.character = Grandpa()
        self.description = "a quiet village where Gilbert lives"

    def give_summary(self):
        pass