from BaseItem import BaseItem


# The currency of the world, used to buy things
class Money(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = "money"
        self.description = "Money; currency of the world, without money you'd have nothing"
        self.amount = 0
