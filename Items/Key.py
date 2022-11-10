from BaseItem import BaseItem


class Key(BaseItem):
    def __init__(self):
        self.name = "key"
        self.description = "Key; A rusty brown key, commonly used for opening doors"
        self.used = False
