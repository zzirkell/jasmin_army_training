class Cow:
    def __init__(self, name, speed):
        self.name = name
        self._speed = speed
        # TODO: store as self._speed
        pass

    # TODO: create @property speed
    @property
    def speed(self):
        return self._speed

    def moo(self):
        return "moo"
