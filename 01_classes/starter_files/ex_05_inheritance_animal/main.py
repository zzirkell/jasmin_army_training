from cow import Cow
from sheep import Sheep
from farm import Farm


def main():
    print("Exercise 05: Inheritance with Animal")
    farm = Farm("Inheritance Farm")
    farm.add_animal(Cow("Bonya"))
    farm.add_animal(Cow("Shusha"))
    farm.add_animal(Sheep("Cloud"))

    for description in farm.describe_all_animals():
        print(description)

    for sound in farm.make_all_sounds():
        print(sound)


if __name__ == "__main__":
    main()
