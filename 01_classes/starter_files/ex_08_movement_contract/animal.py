from abc import ABC, abstractmethod
# TODO: import Movable from movable

class Animal(ABC):
    def __init__(self, name, eyes, legs, speed):
        self.name = name
        self.eyes = eyes
        self.legs = legs
        self.speed = speed

    def move(self):
        # TODO: return movement sentence
        pass

    @abstractmethod
    def make_sound(self):
        pass
