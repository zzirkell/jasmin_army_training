def main():
    invited_people = {"Anna", "Ben", "Clara", "Anna"}
    arrived_people = {"Anna", "Clara"}

    print("Invited people:", invited_people)
    print("Number invited:", len(invited_people))
    print("Arrived people:", arrived_people)

    missing_people = invited_people - arrived_people
    print("Missing people:", missing_people)


if __name__ == "__main__":
    main()
