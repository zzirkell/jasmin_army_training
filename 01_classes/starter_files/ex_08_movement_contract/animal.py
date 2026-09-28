from abc import ABC, abstractmethod
# TODO: import Movable from movable
from movable import Movable

class Animal(Movable, ABC):
    def __init__(self, name, eyes, legs, speed):
        self.name = name
        self.eyes = eyes
        self.legs = legs
        self.speed = speed

    def move(self):
        return f"{self.name} moves with {self.speed} speed."
        # TODO: return movement sentence
        pass

    @abstractmethod
    def make_sound(self):
        pass
