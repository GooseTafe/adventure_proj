from BaseItem import BaseItem


# Cheese used to make the sandwich
class Cheese(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = "cheese"
        self.description = "Cheese; the creamiest of cheeses that melts in your mouth"
        self.used = False
