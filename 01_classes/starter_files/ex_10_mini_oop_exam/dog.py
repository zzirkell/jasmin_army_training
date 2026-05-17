from animal import Animal

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, eyes=2, legs=4, speed=8)

    def make_sound(self):
        return "woof"
