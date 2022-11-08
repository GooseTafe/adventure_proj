from Locations.BaseLocation import BaseLocation


class Forest2(BaseLocation):
    def __init__(self):
        self.character = None
        self.description = "lush green trees everywhere again"

    def give_summary(self):
        print(self.description)
