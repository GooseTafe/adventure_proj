import typing
from abc import abstractmethod, ABC
from Characters.BaseCharacter import BaseCharacter


class BaseLocation(ABC):

    def __init__(self):
        self.character: typing.Union[BaseCharacter, None] = None
        self.description = "this is a location"
        self.item = None

    @abstractmethod
    def give_summary(self):
        pass


