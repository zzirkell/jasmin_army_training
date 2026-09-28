from animal import Animal


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, eyes=2, legs=4, speed=4, sound="moo")
        # TODO: call super().__init__(name, 2, 4, 4, "moo")
        pass
