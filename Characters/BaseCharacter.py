from abc import abstractmethod, ABC


# What all character class skeletons are based on
class BaseCharacter(ABC):

    def __init__(self):
        self.name = "character name"
        self.description = "character description"
        self.items = None
        self.life = None
        self.condition = None
        self.enemy = None
        self.dead = None

    def prompts(self, bag):
        pass

    def pre_attack_phase(self):
        pass

    def attack_response(self, blocked):
        pass

    def item_drop(self, bag):
        pass
