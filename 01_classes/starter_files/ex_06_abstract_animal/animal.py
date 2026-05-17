# TODO: import ABC and abstractmethod from abc


class Animal:
    def __init__(self, name, eyes, legs, speed):
        self.name = name
        self.eyes = eyes
        self.legs = legs
        self.speed = speed

    def run(self):
        return self.speed

    # TODO: make this method abstract
    def make_sound(self):
        pass

    def describe(self):
        return f"{self.name} has {self.eyes} eyes, {self.legs} legs, and speed {self.speed}."
