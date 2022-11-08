from Locations.BaseLocation import BaseLocation
from Characters.GnomeMiner import GnomeMiner


class Cave(BaseLocation):
    def __init__(self):
        self.description = "A cave in the mountain, it does not look naturally made"
        self.character = GnomeMiner()

    def give_summary(self):
        pass