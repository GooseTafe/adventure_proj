from BaseItem import BaseItem


# Vegetables used to make the sandwich
class Vegetables(BaseItem):
    def __init__(self):
        self.name = "vegetables"
        self.description = "Vegetables; edible leaves found in the forest"
        self.used = False
