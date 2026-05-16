def main():
    registered_students = {"Anna", "Sofia", "Lena", "Sofia"}
    attended_students = {"Sofia", "Lena"}
    print("Registered students:", registered_students)
    print("Number registered", len(registered_students))
    print("Attended students:", attended_students)
    print("Missing students:", registered_students - attended_students)
    pass


if __name__ == "__main__":
    main()
