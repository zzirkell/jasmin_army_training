from animal import Animal


class Pigeon(Animal):
    def __init__(self, name):
        super().__init__(name, eyes=2, legs=2, speed=2)
        # TODO: choose eyes, legs, speed
        # Example: super().__init__(name, eyes=2, legs=4, speed=6)
        pass

    def make_sound(self):
        return "ooo"
        # TODO: return your animal sound
        pass
