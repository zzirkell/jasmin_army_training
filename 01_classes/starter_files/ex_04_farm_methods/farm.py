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
        cow_count = len(self.cows)
        sheep_count = len(self.sheep)
        return cow_count + sheep_count
        # TODO: return count of cows + sheep

    def count_all_legs(self):
        leg_count = 0
        for cow in self.cows:
            leg_count = leg_count + cow.legs
        for sheep in self.sheep:
            leg_count = leg_count + sheep.legs
        return leg_count
        # TODO: loop through all animals and add legs

    def calculate_total_speed(self):
        total_speed = 0
        for cow in self.cows:
            total_speed = total_speed + cow.speed
        for sheep in self.sheep:
            total_speed = total_speed + sheep.speed
        return total_speed
        # TODO: loop through all animals and add speed

    def find_fast_animals(self, minimum_speed):
        fast_animals = []
        for cow in self.cows:
            if cow.speed >= minimum_speed:
                fast_animals.append(cow.name)
        for sheep in self.sheep:
            if sheep.speed >= minimum_speed:
                fast_animals.append(sheep.name)
        return fast_animals
        # TODO: return names where speed >= minimum_speed