class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def move_all_animals(self):
        movements = []
        for animal in self.animals:
            movements.append(animal.move())
        return movements
