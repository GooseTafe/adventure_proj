from BaseItem import BaseItem


class Meat(BaseItem):
    def __init__(self):
        self.name = "meat"
        self.description = "Meat; Prime grade juicy red meat freshly butchered from the king boar"
        self.used = False

