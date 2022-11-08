from Items import Minerals, Money
from Characters.BaseCharacter import BaseCharacter


class GnomeMiner(BaseCharacter):
    def __init__(self):
        self.name = "miner"
        self.description = "Standing at less than 3ft tall, a long white beard, endowed with a miners helmet and " \
                           "torch, and brandishing a well used iron pickaxe. "
        self.items = [] # TODO: add items that can be found on the villager
        self.life = 3
        self.condition = False

    def prompts(self):
        exiter = False
        print("Gnome Miner: HOW DID YOU GET IN HERE? WHO ARE YOU? WHAT DO YOU WANT?")
        print("Gilbert explains he found this cave and wandered in")
        print("Gnome Miner: WELL THAT'S HOW YOU GET YOURSELF KILLED BOY....")
        print("Gnome Miner: SINCE YOU'RE HERE YOU WOULDN'T HAVE FOUND A KEY ANYWHERE WOULD YOU?")
        print("Gnome Miner: i DROPPED IT ON MY WAY SOMEWHERE FROM THE VILLAGE TO THIS HERE CAVE")
        print("Gnome Miner: AND I NEED IT TO OPEN THE DOOR TO THE MINE IN THIS CAVE")
        print("Gilbert checks his bag to see if he picked up a key...")
        # TODO: add bag search to search for key in bag