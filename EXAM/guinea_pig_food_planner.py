"""
Mini Exam 01: Guinea Pig Food Planner

Theme:
Bonya and Shusha need a food plan.

Goal:
Use dictionaries, lists, loops, conditions, and functions.

No classes yet.
"""


def calculate_total_food(food_amounts):
    total_food = 0
    for values in food_amounts.values():
        total_food += values
    return total_food

def find_favorite_foods(preferences, minimum_score):
    favorites = []
    for key, value in preferences.items():
        if value >= minimum_score:
            favorites.append(key)
    return favorites


def is_food_plan_enough(total_food, required_food):
    return total_food >= required_food

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