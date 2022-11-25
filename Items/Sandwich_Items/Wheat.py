from BaseItem import BaseItem


# Wheat used to make the sandwich
class Wheat(BaseItem):
    def __init__(self):
        self.name = "wheat"
        self.description = "Wheat; A bunch of golden strands of wheat grown from the ground"
        self.used = False
