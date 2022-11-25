from Locations.BaseLocation import BaseLocation


class Forest(BaseLocation):
    def __init__(self):
        super().__init__()
        self.name = "Forest"
        self.character = None
        self.description = """lush green trees everywhere
There are exits in all directions"""
        self.exits = {'n', 'e', 's', 'w'}
        self.visited = False