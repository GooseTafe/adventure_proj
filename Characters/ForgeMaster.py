from Items.Money import Money
from Characters.BaseCharacter import BaseCharacter
from util import sprint
from Items.Sandwich_Items.Meat import Meat
from Items.Sandwich_Items.Minerals import Minerals
from Items.Sandwich_Items.Wheat import Wheat
from Items.Sandwich_Items.Vegetables import Vegetables
from Items.Sandwich_Items.Cheese import Cheese
from Items.Cooking_Tools import CookingTools


# The Forge Master found in the Forge location
# Purpose is to enable the player to craft the game objective under certain conditions
class ForgeMaster(BaseCharacter):
    def __init__(self):
        self.name = "forgemaster"
        self.description = """An extremely hairy short stature dwarf dressed in a leather apron, gloves, and metal 
        welding helmet (I wonder how he has not caught on fire yet?) """
        self.items = [] # TODO: add items that can be found on the Forge Master
        self.life = 3
        self.condition = False
        self.ingredients = [Meat(), Minerals(), Wheat(), Vegetables(), Cheese(), CookingTools()]

    # checks the player inventory to see if all required items have been collected
    # if one item is left out the check fails and lets the player know whats missing
    def inventory_check(self, bag):
        adventurer_bag = bag
        sprint("Gilbert puts what he has in his bag on the table")
        if adventurer_bag.search_inventory("meat") == self.ingredients[0].name:
            meat = True
            sprint(f"Gilbert puts {self.ingredients[0].description} onto the table")
        else:
            meat = False
            sprint("Gilbert has no Meat")
        if adventurer_bag.search_inventory("cheese") == self.ingredients[4].name:
            cheese = True
            sprint(f"Gilbert puts {self.ingredients[4].description} onto the table")
        else:
            cheese = False
            sprint("Gilbert has no Cheese")
        if adventurer_bag.search_inventory("minerals") == self.ingredients[1].name:
            minerals = True
            sprint(f"Gilbert puts {self.ingredients[1].description} onto the table")
        else:
            minerals = False
        if adventurer_bag.search_inventory("vegetables") == self.ingredients[3].name:
            vegetables = True
            sprint(f"Gilbert puts {self.ingredients[3].description} onto the table")
        else:
            vegetables = False
            sprint("Gilbert has no Vegetables")
        if adventurer_bag.search_inventory("wheat") == self.ingredients[2].name:
            wheat = True
            sprint(f"Gilbert puts {self.ingredients[2].description} onto the table")
        else:
            wheat = False
            sprint("Gilbert has no Wheat")

        if (meat and cheese and minerals and vegetables and wheat) is True:
            return True
        else:
            return False

    # The Dialog and interactions for the Forge Master
    def prompts(self, bag):
        adventurer_bag = bag

        exiter = True
        sprint("""Forge Master: HO HO HO *BUURRPRP* Who do we have here?
        Forge Master: Gilbert you say? Well *BUURRPPP* G-Giblert what can i do for you?
        Gilbert inquires into using the Forge Master's mighty forge to create the perfect sandwich.
        Forge Master: sure I'll allow you to use my forge, only if you have the right tools.""")
        # TODO: search for Minerals in inventory to allow conversation to continue
        if self.inventory_check(adventurer_bag) is True:
            sprint("Forge Master: WOOHOO jolly *BBUURRPP* jolly good, you're free to use whatever you need.")
        else:
            sprint("Forge Master: Unfortunately you do not have all the items you need, come back again when you do.")
