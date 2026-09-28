class Animal:
    def __init__(self, name, eyes, legs, speed, sound):
        self.name = name
        self.eyes = eyes
        self.legs = legs
        self.speed = speed
        self.sound = sound
        # TODO: store all parameters as attributes
        pass

    def run(self):
        return self.speed
        # TODO: return speed
        pass

    def make_sound(self):
        return self.sound
        # TODO: return sound
        pass

    def describe(self):
        return f"{self.name} has {self.eyes} eyes, {self.legs} legs, {self.speed} speed and {self.sound} sound."
        # TODO: return sentence with name, eyes, legs, speed, sound
        pass
