from Items.Sandwich_Items.Meat import Meat
from Items.Money import Money
from Characters.BaseCharacter import BaseCharacter
from random import randint
from util import sprint


# King Boar found in the Clearing location
# Purpose is to fight the player and drop meat and money for the player to take
class KingBoar(BaseCharacter):

    def __init__(self):
        super().__init__()
        self.name = "KingBoar"
        self.description = "A rare Gigantic Boar, covered in scars and battle wounds, tusks as long as your " \
                           "arm, and as thick as your leg."
        self.items = [Money(), Meat()]
        self.life = 3
        self.condition = False
        self.enemy = True
        self.dead = False

    # what gets printed when the player talks to the character
    def prompts(self, bag):
        adventurer_bag = bag
        exiter = True
        sprint(["King Boar: GROOOOAAARRRRRR (its a boar....it cant talk)",
                "Would you like to attack King Boar?: "
                ])
        # asks for the option to attack the boar or not
        while exiter is True:
            choice = input("> ")
            if choice == 'y':
                print("Gilbert draws his sword to attack the boar")
                exiter = False
            elif choice == 'n':
                print("Gilbert leaves the boar alone...for now")
                exiter = False
            else:
                print("invalid choice, please enter: y = yes | n = no")

    # Before the boar attacks it gives a forewarning to the player
    def pre_attack_phase(self):
        sprint(f"""{self.name} is preparing to charge... """)

    # after the pre_attack_phase this contains the main attack and returns the damage value
    # depending on whether blocked is True or False
    def attack_response(self, blocked):
        damage = randint(0, 10)
        less_damage = randint(0, 5)
        # reduce damage if blocked is true
        if blocked is True:
            if less_damage == 0:
                sprint(f"Gilbert avoids {self.name}'s attack, no damage dealt")
            else:
                sprint(f"""{self.name} attempts to charge and jab at Gilbert with it's giant
                            tusks, but Gilbert raises his shield to block the attack
                            dealing {less_damage}""")
                return less_damage
        # normal damage if blocked is false
        elif blocked is False:
            if damage == 0:
                sprint(f"{self.name} misses Gilbert dealing {damage}")
                return damage
            else:
                sprint(f"{self.name} charges Gilbert tossing Gilbert aside dealing {damage}")
                return damage
        else:
            if damage == 0:
                sprint("Gilbert barely avoids the charge and rolls out of the way taking no damage ")
            else:
                sprint(f"""{self.name} charges Gilbert dealing {damage} to Gilbert""")

    # adds the loot to the adventurers bag
    def item_drop(self, bag):
        adventurer_bag = bag
        coins = 5
        sprint(f"Gilbert finds {coins} coins and {self.items[1].description}... and adds them to his bag")
        adventurer_bag.add_item(self.items[0].name)
        adventurer_bag.add_item(self.items[1].name)
        adventurer_bag.money = coins
        return adventurer_bag
