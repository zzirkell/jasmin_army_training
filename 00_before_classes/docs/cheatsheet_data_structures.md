## Useful List, Dictionary, and Set Operations

### `len()`

`len()` gives the number of items.

```python
names = ["Anna", "Ben", "Clara"]

print(len(names))  # 3
```

Works with lists, dictionaries, sets, and strings.

```python
text = "hello"
print(len(text))  # 5
```

---

## Lists

A list stores many values in order.

```python
numbers = [10, 20, 30]
```

### Check if a value is inside a list

```python
numbers = [10, 20, 30]

print(20 in numbers)      # True
print(99 in numbers)      # False
print(99 not in numbers)  # True
```

### Add item

```python
numbers.append(40)
print(numbers)  # [10, 20, 30, 40]
```

### Get item by index

```python
print(numbers[0])  # first item
print(numbers[1])  # second item
```

Important: list indexes start at `0`.

### Loop through list

```python
for number in numbers:
    print(number)
```

---

## Dictionaries

A dictionary stores key-value pairs.

```python
person = {
    "name": "Anna",
    "age": 21
}
```

### Get value by key

```python
print(person["name"])  # Anna
```

### Check if key exists

```python
print("name" in person)     # True
print("height" in person)   # False
```

Important: `in` checks keys, not values.

```python
print("Anna" in person)  # False
```

### Add or change value

```python
person["age"] = 22
person["city"] = "Berlin"
```

### Loop through dictionary keys

```python
for key in person:
    print(key)
```

### Loop through keys and values

```python
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## Sets

A set stores unique values.

```python
colors = {"red", "blue", "green"}
```

### Check if value exists

```python
print("red" in colors)     # True
print("yellow" in colors)  # False
```

### Add item

```python
colors.add("yellow")
```

### Remove item

```python
colors.remove("blue")
```

### Important: sets do not keep order

This means you should not use indexes with sets.

Wrong:

```python
print(colors[0])
```

Sets are useful when you only care whether something exists or not.

---

## Quick Table

```text
len(items)          number of items
x in items          check if x exists
x not in items      check if x does not exist

list.append(x)      add x to list
dict[key]           get value from dictionary
dict.items()        loop through key-value pairs
set.add(x)          add x to set
set.remove(x)       remove x from set
```