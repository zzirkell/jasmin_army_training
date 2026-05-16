"""
Example 13: Calculations Pro

This file shows similar ideas to the exercise,
but with different values.

Do not copy the solution directly.
Use this file to understand the syntax.
"""


def main():
    print("Example 13: Calculations Pro")
    print("----------------------------")

    total_candies = 29
    candies_per_bag = 6

    exact_bags = total_candies / candies_per_bag
    full_bags = total_candies // candies_per_bag
    candies_left = total_candies % candies_per_bag

    print(f"Total candies: {total_candies}")
    print(f"Candies per bag: {candies_per_bag}")
    print(f"Exact number of bags: {exact_bags}")
    print(f"Full bags: {full_bags}")
    print(f"Candies left: {candies_left}")

    print()

    number = -12
    positive_distance = abs(number)
    print(f"abs({number}) is {positive_distance}")

    print()

    scores = [8, 10, 6, 9]

    lowest_score = min(scores)
    highest_score = max(scores)
    total_score = sum(scores)
    average_score = total_score / len(scores)

    print(f"Scores: {scores}")
    print(f"Lowest score: {lowest_score}")
    print(f"Highest score: {highest_score}")
    print(f"Total score: {total_score}")
    print(f"Average score: {round(average_score, 2)}")

    print()

    base = 3
    exponent = 4
    result = pow(base, exponent)

    print(f"{base} to the power of {exponent} is {result}")

    print()

    original_price = 50
    discount_percent = 20

    discount_amount = original_price * discount_percent / 100
    final_price = original_price - discount_amount

    print(f"Original price: {original_price}")
    print(f"Discount: {discount_percent}%")
    print(f"Discount amount: {discount_amount}")
    print(f"Final price: {final_price}")


if __name__ == "__main__":
    main()