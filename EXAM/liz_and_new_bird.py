"""
Mini Exam 02: Liz and the Blue Bird Practice Tracker

Theme:
A small music practice tracker inspired by Liz and the Blue Bird.

Goal:
Use lists, dictionaries, loops, conditions, math, and functions.

No classes yet.
"""


def calculate_total_minutes(practice_minutes):
    """
    practice_minutes is a list of numbers.

    Example:
    [30, 45, 20]

    Return the total number of practice minutes.
    """

    # TODO:
    # Create total = 0.
    # Loop through practice_minutes.
    # Add every number to total.
    # Return total.

    pass


def find_difficult_pieces(piece_difficulties, minimum_difficulty):
    """
    piece_difficulties is a dictionary.

    Example:
    {
        "solo": 9,
        "duet": 6
    }

    Return a list of piece names where difficulty is >= minimum_difficulty.
    """

    # TODO:
    # Create an empty list.
    # Loop through the dictionary using .items().
    # Add difficult pieces to the list.
    # Return the list.

    pass


def has_practiced_enough(total_minutes, target_minutes):
    """
    Return True if total_minutes is >= target_minutes.
    Otherwise return False.
    """

    # TODO:
    # Compare total_minutes and target_minutes.

    pass


def main():
    print("Mini Exam 02: Liz and the Blue Bird Practice Tracker")
    print("----------------------------------------------------")

    practice_minutes = [25, 40, 35, 20, 50]

    piece_difficulties = {
        "oboe solo": 9,
        "flute melody": 7,
        "duet part": 8,
        "warmup": 3
    }

    target_minutes = 150

    total_minutes = calculate_total_minutes(practice_minutes)
    difficult_pieces = find_difficult_pieces(piece_difficulties, 8)
    enough_practice = has_practiced_enough(total_minutes, target_minutes)

    print(f"Total practice time: {total_minutes} minutes")
    print(f"Difficult pieces: {difficult_pieces}")

    if enough_practice:
        print("Practice goal reached.")
    else:
        missing_minutes = target_minutes - total_minutes
        print(f"Practice goal not reached. Missing minutes: {missing_minutes}")


if __name__ == "__main__":
    main()