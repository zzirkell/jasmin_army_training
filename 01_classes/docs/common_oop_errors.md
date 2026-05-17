# Common OOP Errors

## Forgetting `self`

Wrong:

```python
class Cow:
    def moo():
        return "moo"
```

Correct:

```python
class Cow:
    def moo(self):
        return "moo"
```

## Forgetting `self.`

Wrong:

```python
class Cow:
    def __init__(self, name):
        name = name
```

Correct:

```python
class Cow:
    def __init__(self, name):
        self.name = name
```

## Forgetting parentheses when calling a method

Wrong:

```python
print(cow.moo)
```

Correct:

```python
print(cow.moo())
```

## Using a list like one object

Wrong:

```python
cows = [Cow("Bonya"), Cow("Shusha")]
print(cows.moo())
```

Correct:

```python
for cow in cows:
    print(cow.moo())
```

## Returning too early inside a loop

Wrong:

```python
def make_all_sounds(self):
    for animal in self.animals:
        return animal.make_sound()
```

Correct:

```python
def make_all_sounds(self):
    sounds = []
    for animal in self.animals:
        sounds.append(animal.make_sound())
    return sounds
```

## Child class forgot `super().__init__`

Wrong:

```python
class Cow(Animal):
    def __init__(self, name):
        self.sound = "moo"
```

Correct:

```python
class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, eyes=2, legs=4, speed=4)
```
