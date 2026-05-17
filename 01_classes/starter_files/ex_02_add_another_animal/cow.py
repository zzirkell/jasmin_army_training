class Cow:
    def __init__(self, name):
        self.name = name
        self.eyes = 2
        self.legs = 4
        self.speed = 4

    def moo(self):
        return "moo"

    def run(self):
        return self.speed

    def describe(self):
        return f"{self.name} has {self.eyes} eyes, {self.legs} legs, and speed {self.speed}."
