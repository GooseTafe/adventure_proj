from BaseItem import BaseItem


# Cooking tools used to eat the sandwich
class CookingTools(BaseItem):
    def __init__(self):
        self.name = "utensils"
        self.description = "Cooking Utensils; tools used for creating food"
        self.used = False