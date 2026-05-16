"""
Exercise 09A: For Loops with Range

Goal:
Practice repeating code using for-loops and range().

You will practice:
- for-loops
- range(start, stop)
- counting numbers
- using a loop variable
- adding numbers inside a loop

Run this file with:

    python ex_09a_for_loops_with_range.py
"""


def main():
    print("Exercise 09A: For Loops with Range")
    print("----------------------------------")

    for number in range (0, 6):
        print(number)
    print()

    for number in range(1, 11):
        print(number)
    print()
    # Print the sentence "I am learning Python" 5 times.
    for i in range (0, 5):
        print("Your mama is gay")
    print()

    for number in range(0, 11, 2):
        print(number)
    print()

    for number in range(10, 0, -1):
        print(number)
    print()

    total = 0
    for number in range(1, 6):
        total = total + number
    print(total)
    print()

    count = 0
    for i in range (0, 4):
        count = count + 1
    print(count)
    print()

    number = 3
    for multiplier in range (1, 11):
        multiplication = number * multiplier
        print(f"{number} x {multiplier} = {multiplication}")

    pass

if __name__ == "__main__":
    main()