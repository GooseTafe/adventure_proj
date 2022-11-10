from BaseItem import BaseItem


class Wheat(BaseItem):
    def __init__(self):
        self.name = "wheat"
        self.description = "Wheat; A sea of golden strands of wheat growing from the ground"
        self.used = False
