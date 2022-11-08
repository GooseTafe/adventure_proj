from Items.Sandwich_Items import Meat
from Items import Money
from Characters.BaseCharacter import BaseCharacter


class KingBoar(BaseCharacter):
    def __init__(self):
        self.name = "kingboar"
        self.description = "A rare Gigantic Boar, covered in scars and battle wounds, tusks as long as your " \
                           "arm, and as thick as your leg."
        self.items = []  # TODO: add items that can be found on the villager
        self.life = 5
        self.condition = False

    def prompts(self):
        exiter = True
        print("King Boar: GROOOOAAARRRRRR (its a boar....it cant talk)")
        print("Would you like to attack the King Boar?: ")
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
