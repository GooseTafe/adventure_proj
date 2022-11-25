from Locations.BaseLocation import BaseLocation
from Characters.ForgeMaster import ForgeMaster


# The forge that hosts the fore master
class Forge(BaseLocation):
    def __init__(self):
        super().__init__()
        self.name = "Forge"
        self.character = ForgeMaster()
        self.description = f"""A large forge used for creating tools and weapons using the heat of the lava emitted \
         from the volcano sitting on a barrel with a mug swaying side to side looks to be a {self.character.name}.
The only exit available is East."""
        self.exits = {'e'}
        self.visited = False