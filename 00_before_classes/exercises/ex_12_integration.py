def is_passing(grade):
    return grade >= 50
    # TODO: Return True if grade is at least 50, otherwise False.
    pass


def main():
    course_name = "Software Engineering"
    max_students = 3
    students = ["Sofia", "Lena", "Anna", "Sofia"]
    grades = {
        "Sofia": 82,
        "Lena": 49,
        "Anna": 76
    }

    student_list = set(students)
    course_full = len(student_list) == max_students
    print(f"Course: {course_name}\nUnique students: {len(student_list)}\nCourse full: {course_full}")

    for key, value in grades.items():
        print(f"{key} passed: {is_passing(value)}")

    pass


if __name__ == "__main__":
    main()
