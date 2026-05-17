"""
Mini Exam 04: The Chaotic Bike Repair Decision

Theme:
A very questionable bike that maybe should finally be replaced.

Goal:
Use dictionaries, lists, loops, conditions, percentages, and functions.

No classes yet.
"""


def calculate_total_repair_cost(repairs):
    total_cost = 0
    for key, value in repairs.items():
        total_cost += value
    return total_cost

def find_critical_problems(problem_levels, minimum_level):
    critical_problems = []
    for key, value in problem_levels.items():
        if value >= minimum_level:
            critical_problems.append(key)
    return critical_problems


def should_replace_bike(total_cost, bike_value):
    return total_cost > bike_value * 0.5

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