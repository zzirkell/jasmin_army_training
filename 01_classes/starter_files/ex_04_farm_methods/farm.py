class Farm:
    def __init__(self, name):
        self.name = name
        self.cows = []
        self.sheep = []

    def add_cow(self, cow):
        self.cows.append(cow)

    def add_sheep(self, sheep):
        self.sheep.append(sheep)

    def count_all_animals(self):
        # TODO: return count of cows + sheep
        pass

    def count_all_legs(self):
        # TODO: loop through all animals and add legs
        pass

    def calculate_total_speed(self):
        # TODO: loop through all animals and add speed
        pass

    def find_fast_animals(self, minimum_speed):
        # TODO: return names where speed >= minimum_speed
        pass
