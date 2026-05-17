"""
Mini Exam 02: Liz and the Blue Bird Practice Tracker

Theme:
A small music practice tracker inspired by Liz and the Blue Bird.

Goal:
Use lists, dictionaries, loops, conditions, math, and functions.

No classes yet.
"""


def calculate_total_minutes(practice_minutes):
    total_minutes = 0
    for minute in practice_minutes:
        total_minutes += minute
    return total_minutes

def find_difficult_pieces(piece_difficulties, minimum_difficulty):
    difficult_pieces = []
    for piece, difficulty in piece_difficulties.items():
        if difficulty >= minimum_difficulty:
            difficult_pieces.append(piece)
    return difficult_pieces

def has_practiced_enough(total_minutes, target_minutes):
    return total_minutes >= target_minutes

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