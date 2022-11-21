import typing
from abc import abstractmethod, ABC
from Characters.BaseCharacter import BaseCharacter


# Skeleton for each location class
class BaseLocation(ABC):

    def __init__(self):
        self.name = ""
        self.character: typing.Union[BaseCharacter, None] = None
        self.description = "this is a location"
        self.item = None
        self.entrances = {'w'}


