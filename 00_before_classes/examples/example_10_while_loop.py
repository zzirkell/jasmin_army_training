def main():
    current_points = 0
    points_per_day = 10
    goal = 30
    day = 0

    while current_points < goal:
        day = day + 1
        current_points = current_points + points_per_day
        print(f"Day {day}: points = {current_points}")

    print("Goal reached!")


if __name__ == "__main__":
    main()
