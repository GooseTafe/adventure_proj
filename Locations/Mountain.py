from Locations.BaseLocation import BaseLocation
from Items.Key import Key


# Mountain that leads to the cave
class Mountain(BaseLocation):
    def __init__(self):
        super().__init__()
        self.name = "Mountain"
        self.character = None
        self.description = """A perilous mountain that reaches to the heavens.
The only exits are West and South"""
        self.item = Key()
        self.exits = {'w', 's'}
        self.visited = False