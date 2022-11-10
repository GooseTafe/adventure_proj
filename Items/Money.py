from BaseItem import BaseItem


class Money(BaseItem):
    def __init__(self):
        self.name = "money"
        self.description = "Money; currency of the world, without money you'd have nothing"
        self.amount = 0
