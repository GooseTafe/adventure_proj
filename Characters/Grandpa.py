from Characters.BaseCharacter import BaseCharacter


class Grandpa(BaseCharacter):
    def __init__(self):
        self.name = "grandpa"
        self.description = "This is Gilbert's grandfather, he will know details about where to find certain items"
        self.items = []  # TODO: add items that can be found on the villager
        self.life = None  # TODO: add life depending on equipment
        self.condition = False

    def give_character_summary(self):
        pass

    def prompts(self):
        exiter = True
        print("Gilbert starts talking to Grandpa")
        print("Grandpa: Run out of sandwich ingredients again have you aye Gilbert?")
        print("Grandpa: Need me to tell you what you need and where?: ")
        while exiter is True:
            choice = input()
            if choice.lower() == 'y':
                print("Grandpa: What you need for your ingredients are: \n")
                print("1: The most buttery of Cheese, found from the Villager")
                print("2: the rarest of Meat, found from the King Boar")
                print("3: the most golden of wheat, found somewhere in the plains")
                print("4: Only the freshest vegetables, found in the forest")
                exiter = False
            elif choice.lower() == 'n':
                print("Grandpa: Then on your way lad")
                print("Gilbert stops talking to Grandpa")
                exiter = False
            else:
                print("invalid choice, please enter: y = yes | n = no")
