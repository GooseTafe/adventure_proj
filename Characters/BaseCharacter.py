from abc import abstractmethod, ABC


class BaseCharacter(ABC):

    def __init__(self):
        self.name = "character name"
        self.description = "character description"
        self.items = []
        self.life = None
        self.condition = False

    def prompts(self):
        pass