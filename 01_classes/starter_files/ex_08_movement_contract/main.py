from cow import Cow
from sheep import Sheep
from dog import Dog
from farm import Farm


def main():
    print("Exercise 08: Movement Contract")
    farm = Farm("Moving Farm")
    farm.add_animal(Cow("Bonya"))
    farm.add_animal(Sheep("Cloud"))
    farm.add_animal(Dog("Rex"))

    for movement in farm.move_all_animals():
        print(movement)


if __name__ == "__main__":
    main()
