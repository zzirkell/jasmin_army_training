# TODO: import ABC and abstractmethod from abc
from abc import ABC, abstractmethod

class Movable(ABC):
    # TODO: make this method abstract
    @abstractmethod
    def move(self):
        pass
