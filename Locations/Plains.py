from Locations.BaseLocation import BaseLocation
from Characters.Farmer import Farmer
from Items.Money import Money


class Plains(BaseLocation):
    def __init__(self):
        self.character = None
        self.description = "a flat grass land that stretches out across a vast area"
        self.item = Money()

    def give_summary(self):
        pass