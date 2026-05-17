class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def make_all_sounds(self):
        sounds = []
        for animal in self.animals:
            sounds.append(animal.make_sound())
        return sounds

    def describe_all_animals(self):
        descriptions = []
        for animal in self.animals:
            descriptions.append(animal.describe())
        return descriptions
