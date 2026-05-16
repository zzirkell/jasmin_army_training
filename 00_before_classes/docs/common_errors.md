# Common Beginner Errors

## Missing quotes

Wrong:

```python
print(Hello)
```

Correct:

```python
print("Hello")
```
## Common Calculation Errors

### Error: Confusing `/`, `//`, and `%`

These three operators look similar, but they do different things.

```python
print(23 / 5)   # 4.6
print(23 // 5)  # 4
print(23 % 5)   # 3
```

Meaning:

```text
23 / 5 gives the exact result.
23 // 5 gives the number of full groups.
23 % 5 gives what is left.
```

---

### Error: Using `//` when you need a decimal result

Wrong:

```python
total = 23
count = 5

average = total // count
print(average)  # 4
```

Better:

```python
total = 23
count = 5

average = total / count
print(average)  # 4.6
```

Use `/` for averages.

---

### Error: Forgetting that modulo `%` gives the remainder

```python
items = 23
box_size = 5

items_left = items % box_size
print(items_left)  # 3
```

Modulo does not give the division result. It gives what is left.

---

### Error: Forgetting parentheses for built-in functions

Wrong:

```python
numbers = [3, 1, 5]

print(max numbers)
```

Correct:

```python
numbers = [3, 1, 5]

print(max(numbers))
```

Functions need parentheses.

---

## `=` vs `==`

```python
age = 18      # assign value
age == 18     # compare values
```

## Indentation

Wrong:

```python
if grade >= 50:
print("Passed")
```

Correct:

```python
if grade >= 50:
    print("Passed")
```

## Wrong list index

```python
courses = ["A", "B", "C"]
print(courses[0])  # first item
print(courses[2])  # third item
```

Python starts counting from `0`.

## Dictionary key typo

```python
student = {"name": "Sofia"}
print(student["Name"])  # wrong, capital N
```

Dictionary keys must match exactly.

## Infinite while loop

Wrong:

```python
counter = 0
while counter < 3:
    print(counter)
```

Correct:

```python
counter = 0
while counter < 3:
    print(counter)
    counter = counter + 1
```

## Function is defined but not called

```python
def main():
    print("Hello")

if __name__ == "__main__":
    main()
```
