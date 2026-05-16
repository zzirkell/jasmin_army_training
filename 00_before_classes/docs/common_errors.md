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
