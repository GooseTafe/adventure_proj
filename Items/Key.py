from BaseItem import BaseItem


# Key used to open the door in the cave
class Key(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = "key"
        self.description = "Key; A rusty brown key, commonly used for opening doors"
        self.used = False
