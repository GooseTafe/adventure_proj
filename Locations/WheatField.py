from Locations.BaseLocation import BaseLocation
from Characters.Farmer import Farmer


class WheatField(BaseLocation):
    def __init__(self):
        self.description = "A sea of golden wheat expanding across a large area of the plains"
        self.character = Farmer()

    def give_summary(self):
        pass