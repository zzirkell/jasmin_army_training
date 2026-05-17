from cow import Cow
from sheep import Sheep
from dog import Dog
from summer_animal_camp import SummerAnimalCamp


def main():
    print("Exercise 10: Mini OOP Exam")
    camp = SummerAnimalCamp("Exam Camp")
    camp.add_animal(Cow("Bonya"))
    camp.add_animal(Cow("Shusha"))
    camp.add_animal(Sheep("Cloud"))
    camp.add_animal(Dog("Rex"))

    print(f"Number of animals: {camp.count_animals()}")
    print(f"Total legs: {camp.count_total_legs()}")
    print(f"Animals that say moo: {camp.find_animals_by_sound('moo')}")
    print(f"Fast animals: {camp.find_fast_animals(5)}")
    print(camp.camp_report())


if __name__ == "__main__":
    main()
