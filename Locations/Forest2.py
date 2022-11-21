from Locations.BaseLocation import BaseLocation
from Items.Sandwich_Items.Vegetables import Vegetables


# Second instance of the forest
class Forest2(BaseLocation):
    def __init__(self):
        self.name = "Forest2"
        self.character = None
        self.description = "lush green trees everywhere again"
        self.item = Vegetables()
