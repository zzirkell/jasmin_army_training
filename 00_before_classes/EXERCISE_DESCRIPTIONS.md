# 00 Before Classes: 12 Exercises

Originally this was planned as 10 exercises, but basic data structures deserve their own tiny practice files. This module now has 12 exercises so we do not remove loops or functions.

Goal: learn enough Python syntax before classes/OOP starts.

No classes yet. No unit tests yet. No inheritance. No file reading. No advanced Python.

---

## How to work

For each exercise:

1. Run the matching file in `examples/`.
2. Read it slowly.
3. Open the matching file in `exercises/`.
4. Replace the TODOs.
5. Run the exercise file.
6. Compare with the expected output below.

The example is similar, not the same solution.

---

## Good beginner links

- Python MOOC 2026, Part 1: Getting started: https://programming-26.mooc.fi/part-1/1-getting-started/
- Python MOOC 2026 main page: https://programming-26.mooc.fi/
- Python Tutor visualizer: https://pythontutor.com/visualize.html
- Python official tutorial: https://docs.python.org/3/tutorial/index.html
- W3Schools Python lists: https://www.w3schools.com/python/python_lists.asp
- W3Schools Python dictionaries: https://www.w3schools.com/python/python_dictionaries.asp
- W3Schools Python sets: https://www.w3schools.com/python/python_sets.asp
- W3Schools Python conditions: https://www.w3schools.com/python/python_conditions.asp
- W3Schools Python for loops: https://www.w3schools.com/python/python_for_loops.asp
- W3Schools Python functions: https://www.w3schools.com/python/python_functions.asp

Use Python Tutor for loops, dictionaries, sets, and functions. It helps you see what Python stores in memory.

---

# Exercise 1: Print and fixed values

Files:

- Example: `examples/example_01_print_and_values.py`
- Exercise: `exercises/ex_01_print_and_values.py`

Print exactly:

```text
=== Study Plan ===
Student: Maria
Course: Software Engineering
Days left: 14
Goal: Practice Python every day
```

---

# Exercise 2: Variables and basic types

Files:

- Example: `examples/example_02_variables_and_types.py`
- Exercise: `exercises/ex_02_variables_and_types.py`

Create variables for an employee profile and print:

```text
Employee profile
Name: Lena
Department: Marketing
Age: 24
Monthly salary: 3000.5
Full time: False
```

---

# Exercise 3: Strings and f-strings

Files:

- Example: `examples/example_03_strings_and_fstrings.py`
- Exercise: `exercises/ex_03_strings_and_fstrings.py`

Create variables for a customer order and print:

```text
Hello Sofia!
You ordered 3 x Notebook.
Price per item: 4.99
Total price: 14.97
```

Use f-strings for at least two lines.

---

# Exercise 4: Calculations and operators

Files:

- Example: `examples/example_04_calculations.py`
- Exercise: `exercises/ex_04_calculations.py`

Calculate coffee total, cake total, and full total.

Expected output:

```text
Coffee total: 12.8
Cake total: 9.0
Full total: 21.8
```

---

# Exercise 5: List basics

Files:

- Example: `examples/example_05_lists.py`
- Exercise: `exercises/ex_05_lists.py`

Practice an ordered collection.

Expected output:

```text
All courses: ['Management', 'Marketing', 'Software Engineering']
First course: Management
Last course: Software Engineering
Number of courses: 3
After adding: ['Management', 'Marketing', 'Software Engineering', 'Accounting']
```

---

# Exercise 6: Dictionary basics

Files:

- Example: `examples/example_06_dictionaries.py`
- Exercise: `exercises/ex_06_dictionaries.py`

Practice named values using keys.

Create this dictionary:

```python
student = {
    "name": "Sofia",
    "course": "Software Engineering",
    "grade": 76,
    "passed": True
}
```

Print:

```text
Student: Sofia
Course: Software Engineering
Grade: 76
Passed: True
```

Then update the grade to `82` and print:

```text
Updated grade: 82
```

---

# Exercise 7: Set basics

Files:

- Example: `examples/example_07_sets.py`
- Exercise: `exercises/ex_07_sets.py`

Practice unique values.

Create:

```python
registered_students = {"Anna", "Sofia", "Lena", "Sofia"}
attended_students = {"Sofia", "Lena"}
```

Print:

```text
Registered students: {'Anna', 'Lena', 'Sofia'}
Number registered: 3
Attended students: {'Lena', 'Sofia'}
Missing students: {'Anna'}
```

Important: set output order can be different. That is okay.

---

# Exercise 8: Conditions and boolean logic

Files:

- Example: `examples/example_08_conditions_boolean.py`
- Exercise: `exercises/ex_08_conditions_boolean.py`

A customer gets a discount if they are a student and the order is at least 20 euros, OR they have a coupon.

Expected output:

```text
Discount available: True
The customer receives a discount.
```

---

# Exercise 9: For loop over a list

Files:

- Example: `examples/example_09_for_loop.py`
- Exercise: `exercises/ex_09_for_loop.py`

Use a loop to print expenses and calculate total and average.

Expected output:

```text
Expense: 12.5
Expense: 8.99
Expense: 23.4
Expense: 5.0
Total expenses: 49.89
Average expense: 12.4725
```

---

# Exercise 10: While loop

Files:

- Example: `examples/example_10_while_loop.py`
- Exercise: `exercises/ex_10_while_loop.py`

Use a while loop until savings reach a target.

Expected output:

```text
Week 1: savings = 15
Week 2: savings = 30
Week 3: savings = 45
Week 4: savings = 60
Target reached!
```

---

# Exercise 11: Functions and main

Files:

- Example: `examples/example_11_functions.py`
- Exercise: `exercises/ex_11_functions.py`

Write three functions:

```python
calculate_total_price(price, quantity)
is_passing_grade(grade)
create_order_summary(customer_name, product_name, quantity, total_price)
```

Expected output:

```text
Sofia ordered 3 x Notebook for 14.97 euros.
Passing grade: True
```

---

# Exercise 12: Mini integration before classes

Files:

- Example: `examples/example_12_integration.py`
- Exercise: `exercises/ex_12_integration.py`

Use variables, a list, a dictionary, a set, a loop, a condition, and functions.

Scenario: small course registration summary.

Data:

```python
course_name = "Software Engineering"
max_students = 3
students = ["Sofia", "Lena", "Anna", "Sofia"]
grades = {
    "Sofia": 82,
    "Lena": 49,
    "Anna": 76
}
```

Tasks:

1. Make a set from `students` to remove duplicates.
2. Print course name.
3. Print number of unique students.
4. Print whether the course is full.
5. Loop over `grades` and print whether each student passed.

Expected output can have a different order for students because sets/dictionaries can be displayed in different order. One valid output:

```text
Course: Software Engineering
Unique students: 3
Course full: True
Sofia passed: True
Lena passed: False
Anna passed: True
```

---

# After these exercises

Then start:

```text
01_first_classes/
```

First class exercise should be very small:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```
