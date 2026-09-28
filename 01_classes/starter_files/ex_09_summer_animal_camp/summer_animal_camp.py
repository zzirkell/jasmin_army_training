class SummerAnimalCamp:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        return self.animals
        # TODO: add animal
        pass

    def morning_concert(self):
        sounds = []
        for animal in self.animals:
            sounds.append(animal.make_sound())
        return sounds
        # TODO: return list of sounds
        pass

    def morning_run(self):
        run = []
        for animal in self.animals:
            run.append(animal.move())
        return run
        # TODO: return list of movements
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
