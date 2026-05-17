from cow import Cow
from sheep import Sheep
from your_animal import YourAnimal
from farm import Farm


def main():
    print("Exercise 07: Create Your Own Animal")
    farm = Farm("Creative Farm")
    farm.add_animal(Cow("Bonya"))
    farm.add_animal(Sheep("Cloud"))

    # TODO: add your animal
    # farm.add_animal(YourAnimal("Rex"))

    for description in farm.describe_all_animals():
        print(description)
    for sound in farm.make_all_sounds():
        print(sound)


if __name__ == "__main__":
    main()
