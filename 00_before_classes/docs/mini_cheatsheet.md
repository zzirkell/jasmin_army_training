# Mini Cheatsheet Before Classes

## File shape

```python
def main():
    print("Hello")

if __name__ == "__main__":
    main()
```

## Basic types

```python
name = "Anna"        # str
age = 22             # int
price = 12.99        # float
is_student = True    # bool
```

## Print and f-strings

```python
print("Hello")
print("Age:", age)
print(f"{name} is {age} years old")
```

## Operators

```python
total = 10 + 5
remaining = 10 - 5
price = 10 * 3
average = 10 / 2
remainder = 10 % 3
```

## List: ordered collection

```python
courses = ["Management", "Marketing"]
print(courses[0])
courses.append("Accounting")
print(len(courses))
```

Use a list when order matters or duplicates are allowed.

## Dictionary: key-value collection

```python
student = {
    "name": "Sofia",
    "grade": 76
}

print(student["name"])
student["grade"] = 80
```

Use a dictionary when you want named values.

## Set: unique values

```python
tags = {"python", "exam", "python"}
tags.add("oop")
print(tags)
```

Use a set when duplicates should disappear.

## Conditions

```python
if grade >= 50:
    print("Passed")
else:
    print("Failed")
```

## Boolean logic

```python
discount = is_student and order_total >= 20
free_shipping = order_total >= 50 or has_coupon
```

## For loop

```python
total = 0
for price in prices:
    total = total + price
```

## While loop

```python
counter = 0
while counter < 3:
    print(counter)
    counter = counter + 1
```

## Functions

```python
def calculate_total(price, quantity):
    return price * quantity

result = calculate_total(4.99, 3)
```

## The most important beginner questions

1. What type is this value?
2. Is this line inside or outside the loop?
3. Is this line inside or outside the `if`?
4. Does this function `return` or `print`?
5. Did I call the function from `main()`?
