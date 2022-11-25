from Locations.BaseLocation import BaseLocation


# Volcano, a dangerous location that leads to the forge
class Volcano(BaseLocation):
    def __init__(self):
        super().__init__()
        self.name = "Volcano"
        self.character = None
        self.description = """Smaller than the mountain, but more dangerous as lava flows and spews out constantly, be careful.
The only exits are North and West"""
        self.exits = {'n', 'w'}
        self.visited = False