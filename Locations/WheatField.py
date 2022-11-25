from Locations.BaseLocation import BaseLocation
from Characters.Farmer import Farmer
from Items.Sandwich_Items.Wheat import Wheat


# Wheat field where the player can find the Farmer
class WheatField(BaseLocation):
    def __init__(self):
        super().__init__()
        self.name = "WheatField"
        self.character = Farmer()
        self.description = f"""A sea of golden wheat expanding across a large area of the plains. \
Tending to the wheat field is the {self.character.name}
The only exit available is East"""

        self.item = Wheat()
        self.exits = {'e'}
        self.visited = False