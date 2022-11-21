from Locations.BaseLocation import BaseLocation
from Characters.Farmer import Farmer
from Items.Sandwich_Items.Wheat import Wheat


# Wheatfield where the player can find the Farmer
class WheatField(BaseLocation):
    def __init__(self):
        self.name = "WheatField"
        self.description = "A sea of golden wheat expanding across a large area of the plains"
        self.character = Farmer()
        self.item = Wheat()

    def give_summary(self):
        pass