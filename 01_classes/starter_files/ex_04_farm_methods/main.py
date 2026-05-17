from cow import Cow
from sheep import Sheep
from farm import Farm


def main():
    print("Exercise 04: Farm Methods")
    farm = Farm("Calculation Farm")

    farm.add_cow(Cow("Bonya"))
    farm.add_cow(Cow("Shusha"))
    farm.add_cow(Cow("Molly"))
    farm.add_sheep(Sheep("Cloud"))
    farm.add_sheep(Sheep("Snow"))

    print(f"Animals: {farm.count_all_animals()}")
    print(f"Total legs: {farm.count_all_legs()}")
    print(f"Total speed: {farm.calculate_total_speed()}")
    print(f"Fast animals: {farm.find_fast_animals(4)}")


if __name__ == "__main__":
    main()
