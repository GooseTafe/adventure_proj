from abc import abstractmethod, ABC


# skeleton for item classes
class BaseItem(ABC):

    def __init__(self):
        self.name = "item name"
        self.description = "item description"
        self.used = False

