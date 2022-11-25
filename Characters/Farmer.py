from Items.Sandwich_Items.Cheese import Cheese
from Characters.BaseCharacter import BaseCharacter
from util import sprint


# The Farmer that is found in the wheatfields location
# Purpose is to provide the cheese item
class Farmer(BaseCharacter):
    def __init__(self):
        super().__init__()
        self.name = "farmer"
        self.description = "Tanned skin, tall skinny but muscular body, dressed in overalls and wearing a straw hat"
        self.items = Cheese()
        self.life = None
        self.condition = False
        self.enemy = False
        self.dead = False

    # The Dialog and interactions for the farmer
    def prompts(self, bag):
        adventurer_bag = bag
        exiter = True
        price = 3
        sprint("Gilbert starts talking to the Farmer")
        sprint(f"Farmer: why hello there stranger care to buy some fresh cheese for ${price}?: ")
        choice = input("> ")
        while exiter is True:
            if choice == 'y':
                sprint("Gilbert checks his bag for his money")
                #TODO: add money object to bag as well as this statement
                if adventurer_bag.money >= 5:
                    sprint("Farmer: Ahhh wonderful. Thank you here's your cheese")
                    sprint("Gilbert puts the cheese into his bag")
                    adventurer_bag.add_item(self.items.name)

                    adventurer_bag.money = adventurer_bag.money - price
                    sprint(f"Gilbert now has {adventurer_bag.money} coins")
                    return adventurer_bag
                elif adventurer_bag.search_inventory("money") is None:
                    sprint(f"Farmer: It looks to me like you only have {adventurer_bag.money} coins")
                    sprint("Farmer: Come back when you have enough for this delicious creamy cheese")
                    return None
            elif choice == 'n':
                sprint("Farmer: No worries stranger, come back anytime. You know where to find me")
                sprint("Gilbert moves away from the Farmer")
                exiter = False
            else:
                sprint("invalid choice, please enter: y = yes | n = no")
                choice = input("> ")
