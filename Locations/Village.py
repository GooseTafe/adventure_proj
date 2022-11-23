from Locations.BaseLocation import BaseLocation
from Characters.Grandpa import Grandpa


# A village where the player meets the info character grandpa
class Village(BaseLocation):
    def __init__(self):
        self.name = "Village"
        self.character = Grandpa()
        self.description = f"a quiet village where Gilbert lives. Further in town you can see your {self.character.name}"
