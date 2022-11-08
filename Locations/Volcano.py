from Locations.BaseLocation import BaseLocation


class Volcano(BaseLocation):
    def __init__(self):
        self.character = None
        self.description = "Smaller than the mountain, but more dangerous as lava flows and spews out constantly, be careful"

    def give_summary(self):
        pass