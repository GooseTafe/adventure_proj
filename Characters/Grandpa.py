from Characters.BaseCharacter import BaseCharacter
from Items.Shield import Shield


# Grandpa found in the village location
# Purpose is to provide player with information and give the shield item
class Grandpa(BaseCharacter):
    def __init__(self):
        self.name = "grandpa"
        self.description = "This is Gilbert's grandfather, he will know details about where to find certain items"
        self.items = Shield()
        self.life = None
        self.condition = False

    # The Dialog and interactions for Grandpa
    def prompts(self, bag):
        adventurer_bag = bag
        exiter = True
        print("Gilbert starts talking to Grandpa")
        print("Grandpa: Run out of sandwich ingredients again have you aye Gilbert?")
        print("Grandpa: Need me to tell you what you need and where?: ")
        while exiter is True:
            choice = input(">")
            if choice.lower() == 'y':
                print("Grandpa: What you need for your ingredients are: \n")
                print("1: The most buttery of Cheese, found from the Villager")
                print("2: the rarest of Meat, found from the King Boar")
                print("3: the most golden of wheat, found somewhere in the plains")
                print("4: Only the freshest vegetables, found in the forest")
            elif choice.lower() == 'n':
                print("Grandpa: Then on your way lad")
                print("Gilbert stops talking to Grandpa")
            else:
                print("invalid choice, please enter: y = yes | n = no")

            print("Grandpa: That will go nicely with your sword...")
            print("You do have your sword don't you?")
            print("Gilbert checks for his sword")
            if adventurer_bag.search_inventory("sword") == "sword":
                print("Grandpa: Good on you lad, never leave home without your sword")
            elif adventurer_bag.search_inventory("sword") is None:
                print("*Grandpa shakes his head*")
                print("Grandpa: GILBERT YOU FOOL NEVER LEAVE HOME WITHOUT YOUR SWORD, GO BACK AND GET IT!!")
                return None

            print("Grandpa: Oh and before you go I got you this, it'll help with your adventure")
            print("Would you like to take the shield?")
            choice = input("> ")
            if choice.lower() == 'y':
                print("Gilbert obtained a wooden shield from Grandpa!")
                adventurer_bag.add_item(self.items.name)
                return adventurer_bag
            elif choice.lower() == 'n':
                print("Gilbert decides not to take the shield")
            else:
                print("invalid choice, please enter: y = yes | n = no")
            exiter = False

