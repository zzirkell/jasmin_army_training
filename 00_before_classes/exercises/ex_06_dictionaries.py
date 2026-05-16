def main():
    student = {
        "name": "Sofia",
        "course": "Software Engineering",
        "grade": 76,
        "passed": True
    }
    print("Student name:", student["name"])
    print("Student course:", student["course"])
    print("Student grade:", student["grade"])
    print("Passed:", student["passed"])
    student["grade"] = 82
    print("Updated grade:", student["grade"])
    pass


if __name__ == "__main__":
    main()
