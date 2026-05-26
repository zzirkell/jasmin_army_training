from cow import Cow


def main():
    print("Exercise 01: Cows Only")
    bonya = Cow("Bonya")
    shusha = Cow("Shusha")
    molly = Cow("Molly")
    cows = [bonya, shusha, molly]

    for cow in cows:
        print(f"{cow.describe()} {cow.name} has a {cow.moo()} sound and runs with a speed of {cow.run()}")

if __name__ == "__main__":
    main()
