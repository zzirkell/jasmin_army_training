from animal import Animal


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, eyes=2, legs=4, speed=4)

    def make_sound(self):
        # TODO: return "moo"
        pass
