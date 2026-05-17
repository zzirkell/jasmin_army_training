def main():
    savings = 0
    weekly_saving = 16
    target = 60
    week = 0

    while savings < target:
        savings = savings + weekly_saving
        week = week + 1
        print(f"Week {week}: savings = {savings}")
    print("Target reached!")

    pass


if __name__ == "__main__":
    main()
