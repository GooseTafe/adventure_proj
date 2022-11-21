from BaseItem import BaseItem


# Minerals used to make the sandwich
class Minerals(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = "minerals"
        self.description = "Minerals; certain type of rock that can be used in cooking"
        self.used = None