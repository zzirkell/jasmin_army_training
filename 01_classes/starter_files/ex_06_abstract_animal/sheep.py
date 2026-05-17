from animal import Animal


class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, eyes=2, legs=4, speed=3)

    def make_sound(self):
        # TODO: return "baa"
        pass
