"""
Example 09A: For Loops with Range

This file shows how to repeat code using for-loops and range().

Do not copy the solution directly.
Use this file to understand the syntax.
"""


def main():
    print("Example 09A: For Loops with Range")
    print("---------------------------------")

    print("Numbers from 0 to 4:")

    for number in range(0, 5):
        print(number)

    print()

    print("Numbers from 1 to 5:")

    for number in range(1, 6):
        print(number)

    print()

    print("Repeat a sentence 3 times:")

    for i in range(0, 3):
        print("Python is useful")

    print()

    print("Even numbers from 0 to 8:")

    for number in range(0, 9, 2):
        print(number)

    print()

    print("Countdown:")

    for number in range(5, 0, -1):
        print(number)

    print()

    print("Adding numbers from 1 to 4:")

    total = 0

    for number in range(1, 5):
        total = total + number

    print(f"Total: {total}")

    print()

    print("Multiplication table for 2:")

    number = 2

    for multiplier in range(1, 11):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")


if __name__ == "__main__":
    main()