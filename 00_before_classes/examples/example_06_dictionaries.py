def main():
    event = {
        "name": "Python Workshop",
        "room": "B04",
        "duration_minutes": 90,
        "online": False
    }

    print("Event:", event["name"])
    print("Room:", event["room"])
    print("Duration:", event["duration_minutes"])
    print("Online:", event["online"])

    event["room"] = "C20"
    print("Updated room:", event["room"])


if __name__ == "__main__":
    main()
