## `pass`

`pass` means “do nothing”.

Python uses it when a block of code cannot be empty.

Example:

```python
def main():
    pass
```

This function does nothing, but the code is valid.

In exercises, `pass` is usually a placeholder.

Example:

```python
def calculate_total(numbers):
    # TODO: write code here
    pass
```

Later, replace `pass` with real code:

```python
def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

Important: if you keep `pass`, the function probably does nothing.