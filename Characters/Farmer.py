from Items.Sandwich_Items import Wheat
from Items import Money
from Characters.BaseCharacter import BaseCharacter
from Characters.Adventurer import Adventurer


class Farmer(BaseCharacter):
    def __init__(self):
        self.name = "farmer"
        self.adventurer_bag = Adventurer().bag
        self.description = "Tanned skin, tall skinny but muscular body, dressed in overalls and wearing a straw hat"
        self.items = [] # TODO: add items that can be found on the villager
        self.life = 3
        self.condition = False

    def prompts(self):
        exiter = True
        print("Gilbert starts talking to the Farmer")
        print("Farmer: why hello there stranger care to buy some fresh cheese for $3?: ")
        choice = input("> ")
        while exiter is True:
            if choice == 'y':
                print("Gilbert checks his bag for his money")
                #TODO: add money object to bag as well as this statement
                if self.adventurer_bag.search_inventory("money") is not None:
                    print("Farmer: Ahhh wonderful. Thank you here's your cheese")
                    self.adventurer_bag.items.append("cheese")
                    self.adventurer_bag.items.remove("money")
                exiter = False
            elif choice == 'n':
                print("Farmer: No worries stranger, come back anytime. You know where to find me")
                print("Gilbert moves away from the Farmer")
                exiter = False
            else:
                print("invalid choice, please enter: y = yes | n = no")
