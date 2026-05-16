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

### Common special characters

```text
\n      new line
\t      tab
\"      double quote
\'      single quote
\\      backslash (it is just \)
```

### Examples

```python
print("Name:\tAnna")
print("She said \"hello\"")
print("C:\\Users\\Anna")
```

Output:

```text
Name:   Anna
She said "hello"
C:\Users\Anna
```

### Raw strings for paths (python know to pring whatever is in "", does not see special characters at all)

For file paths, raw strings can be easier:

```python
print(r"C:\Users\Anna")
```

## Operators

```python
total = 10 + 5
remaining = 10 - 5
price = 10 * 3
average = 10 / 2
remainder = 10 % 3
```
## Calculations Pro

### Normal division `/`

Normal division gives a decimal number.

```python
result = 23 / 5
print(result)  # 4.6
```

Use `/` when you want the exact mathematical result.

---

### Integer division `//`

Integer division gives only the whole-number part.

```python
result = 23 // 5
print(result)  # 4
```

Use `//` when you want to know how many full groups fit.

Example:

```python
items = 23
box_size = 5

full_boxes = items // box_size
print(full_boxes)  # 4
```

Meaning: 23 items can fill 4 full boxes of size 5.

---

### Modulo `%`

Modulo gives the remainder.

```python
result = 23 % 5
print(result)  # 3
```

Use `%` when you want to know what is left after division.

Example:

```python
items = 23
box_size = 5

items_left = items % box_size
print(items_left)  # 3
```

Meaning: after filling 4 boxes, 3 items are left.

---

### `/`, `//`, and `%` together

```python
items = 23
box_size = 5

exact_boxes = items / box_size
full_boxes = items // box_size
items_left = items % box_size

print(exact_boxes)  # 4.6
print(full_boxes)   # 4
print(items_left)   # 3
```

Meaning:

```text
23 items can fill 4 full boxes of size 5.
3 items are left.
```

---

### Useful built-in math functions

```python
round(4.678, 2)   # 4.68
abs(-7)           # 7
min([3, 1, 5])    # 1
max([3, 1, 5])    # 5
sum([3, 1, 5])    # 9
pow(2, 3)         # 8
```

### `round()`

```python
price = 12.9876
rounded_price = round(price, 2)

print(rounded_price)  # 12.99
```

### `abs()`

`abs()` gives the distance from zero.

```python
temperature = -7
distance_from_zero = abs(temperature)

print(distance_from_zero)  # 7
```

### `min()`, `max()`, and `sum()`

Useful when working with lists of numbers.

```python
prices = [12.99, 5.50, 3.25, 20.00]

cheapest = min(prices)
most_expensive = max(prices)
total = sum(prices)

print(cheapest)        # 3.25
print(most_expensive)  # 20.0
print(total)           # 41.74
```

### `pow()`

`pow(a, b)` means `a` to the power of `b`.

```python
result = pow(2, 3)
print(result)  # 8
```

This is the same as:

```python
result = 2 ** 3
print(result)  # 8
```

---

### Discount calculation pattern

```python
original_price = 80
discount_percent = 15

discount_amount = original_price * discount_percent / 100
final_price = original_price - discount_amount

print(discount_amount)  # 12.0
print(final_price)      # 68.0
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
## For Loops with `range()`

Use a `for` loop when you want to repeat code.

```python
for number in range(0, 6):
    print(number)
```

Output:

```text
0
1
2
3
4
5
```

Important: `range(0, 6)` stops before `6`.

### Common patterns

```python
range(0, 5)       # 0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5
range(0, 11, 2)   # 0, 2, 4, 6, 8, 10
range(5, 0, -1)   # 5, 4, 3, 2, 1
```

### Repeating code

```python
for i in range(0, 3):
    print("Hello")
```

Output:

```text
Hello
Hello
Hello
```

### Adding numbers in a loop

```python
total = 0

for number in range(1, 6):
    total = total + number

print(total)  # 15
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
