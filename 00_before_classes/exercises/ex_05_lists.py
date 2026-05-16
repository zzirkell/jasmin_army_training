def main():
    courses = ['Management', 'Marketing', 'Software Engineering']
    print("All courses:", courses)
    print("First course:", courses[0])
    print("Last course:", courses[2])
    print("Number of courses:", len(courses))
    courses.append('Accounting')
    print("After adding:", courses)

    pass


if __name__ == "__main__":
    main()
