from Locations.BaseLocation import BaseLocation
from Characters.GnomeMiner import GnomeMiner


class Cave(BaseLocation):
    def __init__(self):
        super().__init__()
        self.name = "Cave"
        self.character = GnomeMiner()
        self.description = f"""A cave in the mountain, it does not look naturally made, but it looks like there is a \
        {self.character.name}.
The only exit available is to the North"""
        self.exits = {'n'}
        self.visited = False