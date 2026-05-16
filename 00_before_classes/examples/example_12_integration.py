def is_passing(grade):
    return grade >= 50


def main():
    workshop_name = "Python Workshop"
    max_participants = 2
    participants = ["Anna", "Ben", "Anna"]
    scores = {
        "Anna": 90,
        "Ben": 45
    }

    unique_participants = set(participants)
    workshop_full = len(unique_participants) >= max_participants

    print("Workshop:", workshop_name)
    print("Unique participants:", len(unique_participants))
    print("Workshop full:", workshop_full)

    for name in scores:
        print(f"{name} passed: {is_passing(scores[name])}")


if __name__ == "__main__":
    main()
