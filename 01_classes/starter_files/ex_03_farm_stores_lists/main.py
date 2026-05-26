from cow import Cow
from sheep import Sheep
from farm import Farm


def main():
    print("Exercise 03: Farm Stores Lists")
    farm = Farm("Tiny Farm")

    farm.add_cow("Aylin")
    farm.add_cow("Ceyda")
    farm.add_cow("Selena")
    farm.add_sheep("Sevgi")
    farm.add_sheep("Mine")

    print(farm.make_cows_moo())
    print(farm.make_sheep_baa())

if __name__ == "__main__":
    main()
