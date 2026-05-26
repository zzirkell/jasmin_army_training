from cow import Cow
from sheep import Sheep


def main():
    print("Exercise 02: Add Another Animal")

    cows = [Cow("Bonya"), Cow("Shusha")]
    sheep_s = [Sheep("Lara"), Sheep("Lena")]

    for cow in cows:
        print(f"{cow.describe()} {cow.name} has sound {cow.moo()} and runs with speed {cow.run()}.")

    for sheep in sheep_s:
        print(f"{sheep.describe()} {sheep.name} has sound {sheep.baa()} and runs with speed {sheep.run()}.")

if __name__ == "__main__":
    main()
