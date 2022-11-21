from BaseItem import BaseItem


# Meat used to make the sandwich
class Meat(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = "meat"
        self.description = "Meat; Prime grade juicy red meat freshly butchered from the king boar"
        self.used = False

