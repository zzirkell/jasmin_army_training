class SummerAnimalCamp:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def count_animals(self):
        animal_count = len(self.animals)
        return animal_count
        # TODO: return number of animals
        pass

    def count_total_legs(self):
        total_legs = 0
        for animal in self.animals:
            total_legs = animal.legs + total_legs
        return total_legs
        # TODO: return total legs
        pass

    def find_animals_by_sound(self, sound):
        animals_by_sound = []
        for animal in self.animals:
            if animal.make_sound() == sound:
                animals_by_sound.append(animal.name)
        return animals_by_sound
        # TODO: return names where make_sound() == sound
        pass

    def find_fast_animals(self, minimum_speed):
        fast_animals = []
        for animal in self.animals:
            if animal.run() >= minimum_speed:
                fast_animals.append(animal.name)
        return fast_animals
        # TODO: return names where speed >= minimum_speed
        pass

    def camp_report(self):
        descriptions = []
        for animal in self.animals:
            descriptions.append(animal.describe())
        return descriptions
        # TODO: return descriptions
        pass
