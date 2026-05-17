from cow import Cow
from sheep import Sheep
from dog import Dog
from summer_animal_camp import SummerAnimalCamp


def main():
    print("Exercise 09: Summer Animal Camp")
    camp = SummerAnimalCamp("Tiny Summer Animal Camp")
    camp.add_animal(Cow("Bonya"))
    camp.add_animal(Sheep("Cloud"))
    camp.add_animal(Dog("Rex"))

    print(camp.camp_report())
    print(camp.morning_concert())
    print(camp.morning_run())
    print(camp.find_fast_animals(5))


if __name__ == "__main__":
    main()
