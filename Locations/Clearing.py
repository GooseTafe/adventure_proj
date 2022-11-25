from Locations.BaseLocation import BaseLocation
from Characters.KingBoar import KingBoar


# A clearing in the forest that hosts the King Boar
class Clearing(BaseLocation):
    def __init__(self):
        super().__init__()
        self.name = "Clearing"
        self.character = KingBoar()
        self.description = f"""a clearing in the forest where light is shining through the trees, on the other side of \
the clearing the {self.character.name} can be seen.
The only exit available is West."""
        self.item = None
        self.exits = {'w'}
