"""
Mini Exam 01: Guinea Pig Food Planner

Theme:
Bonya and Shusha need a food plan.

Goal:
Use dictionaries, lists, loops, conditions, and functions.

No classes yet.
"""


def calculate_total_food(food_amounts):
    """
    food_amounts is a dictionary.

    Example:
    {
        "cucumber": 40,
        "pepper": 30,
        "salad": 50
    }

    Return the total amount of food.
    """

    # TODO:
    # Create total = 0.
    # Loop through the values in food_amounts.
    # Add each amount to total.
    # Return total.

    pass


def find_favorite_foods(preferences, minimum_score):
    """
    preferences is a dictionary.

    Example:
    {
        "cucumber": 10,
        "pepper": 8,
        "carrot": 4
    }

    Return a list with all foods where the score is >= minimum_score.
    """

    # TODO:
    # Create an empty list called favorites.
    # Loop through the dictionary using .items().
    # If the score is high enough, append the food name.
    # Return favorites.

    pass


def is_food_plan_enough(total_food, required_food):
    """
    Return True if total_food is enough.
    Otherwise return False.
    """

    # TODO:
    # Compare total_food and required_food.

    pass


def main():
    print("Mini Exam 01: Guinea Pig Food Planner")
    print("-------------------------------------")

    food_amounts = {
        "cucumber": 40,
        "pepper": 30,
        "salad": 50,
        "carrot": 10
    }

    preferences = {
        "cucumber": 10,
        "pepper": 9,
        "salad": 7,
        "carrot": 4
    }

    required_food = 100

    total_food = calculate_total_food(food_amounts)
    favorite_foods = find_favorite_foods(preferences, 8)
    enough = is_food_plan_enough(total_food, required_food)

    print(f"Total food: {total_food}g")
    print(f"Favorite foods: {favorite_foods}")

    if enough:
        print("Bonya and Shusha have enough food but always need more food.")
    else:
        print("Bonya and Shusha need more food.")


if __name__ == "__main__":
    main()