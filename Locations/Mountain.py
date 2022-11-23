from Locations.BaseLocation import BaseLocation
from Items.Key import Key


# Mountain that leads to the cave
class Mountain(BaseLocation):
    def __init__(self):
        self.name = "Mountain"
        self.character = None
        self.description = "A perilous mountain that reaches to the heavens"
        self.item = Key()

    def give_summary(self):
        pass