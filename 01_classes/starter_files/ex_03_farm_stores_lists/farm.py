class Farm:
    def __init__(self, name):
        self.name = name
        self.cows = []
        self.sheep = []

    def add_cow(self, cow):
        self.cows.append(cow)

    def add_sheep(self, sheep):
        self.sheep.append(sheep)

    def make_cows_moo(self):
        moos = []
        for cow in self.cows:
            moos.append("moo")
        return moos


    def make_sheep_baa(self):
        baas = []
        for sheep in self.sheep:
            baas.append("baa")
        return baas