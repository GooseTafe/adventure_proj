from Items.Sandwich_Items.Cheese import Cheese
from Items.Money import Money
from Characters.BaseCharacter import BaseCharacter


# The Farmer that is found in the wheatfields location
# Purpose is to provide the cheese item
class Farmer(BaseCharacter):
    def __init__(self):
        super().__init__()
        self.name = "farmer"
        self.description = "Tanned skin, tall skinny but muscular body, dressed in overalls and wearing a straw hat"
        self.items = Cheese()
        self.life = 3
        self.condition = False

    # The Dialog and interactions for the farmer
    def prompts(self, bag):
        adventurer_bag = bag
        exiter = True
        print("Gilbert starts talking to the Farmer")
        print("Farmer: why hello there stranger care to buy some fresh cheese for $3?: ")
        choice = input("> ")
        while exiter is True:
            if choice == 'y':
                print("Gilbert checks his bag for his money")
                #TODO: add money object to bag as well as this statement
                if adventurer_bag.search_inventory("money") is not None:
                    print("Farmer: Ahhh wonderful. Thank you here's your cheese")
                    print("Gilbert puts the cheese into his bag")
                    adventurer_bag.add_item(self.items.name)
                    adventurer_bag.items.remove("money")
                    return adventurer_bag
                elif adventurer_bag.search_inventory("money") is None:
                    print("Farmer: It looks to me like you don't have enough money")
                    print("Farmer: Come back when you have enough for this delicious creamy cheese")
                    return None
            elif choice == 'n':
                print("Farmer: No worries stranger, come back anytime. You know where to find me")
                print("Gilbert moves away from the Farmer")
                exiter = False
            else:
                print("invalid choice, please enter: y = yes | n = no")
                choice = input("> ")
