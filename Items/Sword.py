from BaseItem import BaseItem


# Used to inflict greater damage on attackers
class Sword(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = "sword"
        self.description = "Sword; A sharp iron sword the length of an arm, used for attacking foes"



