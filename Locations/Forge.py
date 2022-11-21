from Locations.BaseLocation import BaseLocation
from Characters.ForgeMaster import ForgeMaster


# The forge that hosts the fore master
class Forge(BaseLocation):
    def __init__(self):
        self.name = "Forge"
        self.character = ForgeMaster()
        self.description = "A large forge used for creating tools and weapons using the heat of the lava emitted from the volcano"
