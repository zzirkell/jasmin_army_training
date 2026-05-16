def main():
    rooms = ["A12", "B04", "C20"]

    print("All rooms:", rooms)
    print("First room:", rooms[0])
    print("Last room:", rooms[2])
    print("Number of rooms:", len(rooms))

    rooms.append("D01")
    print("After adding:", rooms)


if __name__ == "__main__":
    main()
