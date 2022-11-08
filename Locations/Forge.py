from Locations.BaseLocation import BaseLocation
from Characters.ForgeMaster import ForgeMaster


class Forge(BaseLocation):
    def __init__(self):
        self.character = ForgeMaster()
        self.description = "A large forge used for creating tools and weapons using the heat of the lava emitted from the volcano"

    def give_summary(self):
        pass