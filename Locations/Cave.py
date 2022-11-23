from Locations.BaseLocation import BaseLocation
from Characters.GnomeMiner import GnomeMiner


class Cave(BaseLocation):
    def __init__(self):
        self.name = "Cave"
        self.character = GnomeMiner()
        self.description = f"A cave in the mountain, it does not look naturally made, but it looks like there is a {self.character.name}"
