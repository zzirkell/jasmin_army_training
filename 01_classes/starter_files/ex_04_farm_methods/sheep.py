class Sheep:
    def __init__(self, name):
        self.name = name
        self.eyes = 2
        self.legs = 4
        self.speed = 3

    def baa(self):
        return "baa"

    def run(self):
        return self.speed

    def describe(self):
        return f"{self.name} the sheep has {self.eyes} eyes, {self.legs} legs, and speed {self.speed}."
