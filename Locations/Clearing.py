from Locations.BaseLocation import BaseLocation
from Characters.KingBoar import KingBoar


# A clearing in the forest that hosts the King Boar
class Clearing(BaseLocation):
    def __init__(self):
        super().__init__()
        self.name = "Clearing"
        self.character = KingBoar()
        self.description = "a clearing in the forest where light is shining through the trees"
        self.item = None
        self.entrances = {}
