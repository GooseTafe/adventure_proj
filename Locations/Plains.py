from Locations.BaseLocation import BaseLocation
from Characters.Farmer import Farmer
from Items.Money import Money


# Plains, the location to lead to the Wheat Field
class Plains(BaseLocation):
    def __init__(self):
        super().__init__()
        self.name = "Plains"
        self.character = None
        self.description = """a flat grass land that stretches out across a vast area.
The only exits available are East and South"""
        self.item = Money()
        self.exits = {'e', 's'}
        self.visited = False