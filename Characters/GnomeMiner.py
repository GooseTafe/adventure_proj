from Items.Sandwich_Items.Minerals import Minerals
from Characters.BaseCharacter import BaseCharacter


# Character Gnome Miner found in the Cave location
# Purpose is to give player minerals on task completion
class GnomeMiner(BaseCharacter):
    def __init__(self):
        super().__init__()
        self.name = "miner"
        self.description = "Standing at less than 3ft tall, a long white beard, endowed with a miners helmet and " \
                           "torch, and brandishing a well used iron pickaxe. "
        self.items = Minerals()
        self.life = None
        self.condition = False
        self.enemy = False
        self.dead = False

    # The Dialog and interactions for the Gnome Miner
    def prompts(self, bag):
        adventurer_bag = bag
        print("Gnome Miner: HOW DID YOU GET IN HERE? WHO ARE YOU? WHAT DO YOU WANT?")
        print("Gilbert explains who he is, what he's doing and how he found this cave and wandered in")
        print("Gnome Miner: WELL THAT'S HOW YOU GET YOURSELF KILLED BOY...")
        print("Gnome Miner: SINCE YOU'RE HERE YOU WOULDN'T HAVE FOUND A KEY ANYWHERE WOULD YOU?")
        print("Gnome Miner: I DROPPED IT ON MY WAY SOMEWHERE FROM THE VILLAGE TO THIS HERE CAVE")
        print("Gnome Miner: AND I NEED IT TO OPEN THE DOOR TO THE MINE IN THIS CAVE")
        print("Gilbert checks his bag to see if he picked up a key...")
        if adventurer_bag.search_inventory("key") == "key":
            print("Gilbert finds the key!")
            print("Gnome Miner: OH BOY, OH YES, YEEPEE YOU HAVE THE KEY")
            print("Gilbert gives the key to the Gnome Miner")
            adventurer_bag.remove_item("key")
            print("The Gnome Miner goes to open the door with the key")
            print("The door slowly creeks open spewing out a billow of loose dust and dirt")
            print("Gnome Miner: THANK YOU SO MUCH GILBERT HERE TAKE THIS")
            print(f"Would you like to take {self.items.name} from the Gnome Miner?")
            while True:
                choice = input()
                if choice.lower() == 'y':
                    print(f"Gilbert obtained {self.items.name} from the Gnome Miner!")
                    adventurer_bag.add_item(self.items.name)
                    return adventurer_bag
                elif choice.lower() == 'n':
                    print(f"Gilbert decides not to take the {self.items.name}")
                    return None
                else:
                    print("invalid choice, please enter: y = yes | n = no")
        else:
            print("Gilbert could not find the key in his bag")
            print("Gnome Miner: BUGGER, DAMNIT. I NEED THAT KEY!")
            print("Gnome Miner: WOULD YOU BE ABLE TO FIND IT FOR ME?")
            print("Gilbert agrees to find the key for the Gnome miner")
            print("Gilbert stops talking with the Gnome Miner")
            return None





