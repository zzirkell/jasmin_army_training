from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, eyes, legs, speed):
        self.name = name
        self.eyes = eyes
        self.legs = legs
        self.speed = speed

    def run(self):
        return self.speed

    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        return f"{self.name} moves with speed {self.speed}."

    def describe(self):
        return f"{self.name} has {self.eyes} eyes, {self.legs} legs, and speed {self.speed}."
