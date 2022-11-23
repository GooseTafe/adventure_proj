from Locations.BaseLocation import BaseLocation
from Characters.Adventurer import Adventurer
from Items.Sword import Sword


# Starting location of adventure
class House(BaseLocation):
    def __init__(self):
        super().__init__()
        self.name = "Home"
        self.description = "Gilbert's house, nothing interesting to speak of as it is just a place to sleep"
        self.character = Adventurer()
        self.item = Sword()

