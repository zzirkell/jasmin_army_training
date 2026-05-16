"""
Mini Exam 04: The Chaotic Bike Repair Decision

Theme:
A very questionable bike that maybe should finally be replaced.

Goal:
Use dictionaries, lists, loops, conditions, percentages, and functions.

No classes yet.
"""


def calculate_total_repair_cost(repairs):
    """
    repairs is a dictionary.

    Example:
    {
        "brakes": 40,
        "chain": 25
    }

    Return the total repair cost.
    """

    # TODO:
    # Create total = 0.
    # Loop through the repair costs.
    # Add each cost to total.
    # Return total.

    pass


def find_critical_problems(problem_levels, minimum_level):
    """
    problem_levels is a dictionary.

    Example:
    {
        "brakes": 10,
        "bell": 2
    }

    Return a list of problems where the level is >= minimum_level.
    """

    # TODO:
    # Create an empty list.
    # Loop through problem_levels using .items().
    # Add critical problem names to the list.
    # Return the list.

    pass


def should_replace_bike(total_cost, bike_value):
    """
    Return True if repair cost is more than 50% of the bike value.
    Otherwise return False.
    """

    # TODO:
    # Calculate half of the bike value.
    # Return True if total_cost is greater than that.
    # Otherwise return False.

    pass


def main():
    print("Mini Exam 04: The Chaotic Bike Repair Decision")
    print("----------------------------------------------")

    repairs = {
        "brakes": 45,
        "chain": 25,
        "front light": 15,
        "tire": 35,
        "mysterious noise": 20
    }

    problem_levels = {
        "brakes": 10,
        "chain": 6,
        "front light": 4,
        "tire": 8,
        "mysterious noise": 9
    }

    bike_value = 180

    total_cost = calculate_total_repair_cost(repairs)
    critical_problems = find_critical_problems(problem_levels, 8)
    replace = should_replace_bike(total_cost, bike_value)

    print(f"Total repair cost: {total_cost} euros")
    print(f"Bike value: {bike_value} euros")
    print(f"Critical problems: {critical_problems}")

    repair_percentage = total_cost / bike_value * 100
    print(f"Repair cost is {round(repair_percentage, 1)}% of the bike value.")

    if replace:
        print("Decision: maybe it is time to throw the bike away.")
    else:
        print("Decision: repairing the bike is still reasonable.")


if __name__ == "__main__":
    main()