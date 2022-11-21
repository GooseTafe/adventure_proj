from Locations.BaseLocation import BaseLocation


class Forest(BaseLocation):
    def __init__(self):
        self.name = "Forest"
        self.character = None
        self.description = "lush green trees everywhere"

    def give_summary(self):
        print(self.description)
