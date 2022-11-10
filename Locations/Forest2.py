from Locations.BaseLocation import BaseLocation
from Items.Sandwich_Items.Vegetables import Vegetables

class Forest2(BaseLocation):
    def __init__(self):
        self.character = None
        self.description = "lush green trees everywhere again"
        self.item = Vegetables()
    def give_summary(self):
        print(self.description)
