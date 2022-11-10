from BaseItem import BaseItem


class CookingTools(BaseItem):
    def __init__(self):
        self.name = "utensils"
        self.description = "Cooking Utensils; tools used for creating food"
        self.used = False