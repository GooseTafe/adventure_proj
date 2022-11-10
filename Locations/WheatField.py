from Locations.BaseLocation import BaseLocation
from Characters.Farmer import Farmer
from Items.Sandwich_Items.Wheat import Wheat


class WheatField(BaseLocation):
    def __init__(self):
        self.description = "A sea of golden wheat expanding across a large area of the plains"
        self.character = Farmer()
        self.item = Wheat()

    def give_summary(self):
        pass