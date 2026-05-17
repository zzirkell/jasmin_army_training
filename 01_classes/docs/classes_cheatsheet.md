# Classes Cheatsheet

## Class

A class is a blueprint.

```python
class Cow:
    pass
```

## Object

An object is one concrete thing created from a class.

```python
cow = Cow()
```

## `__init__`

`__init__` runs when the object is created.

```python
class Cow:
    def __init__(self, name):
        self.name = name
```

```python
cow = Cow("Bonya")
```

## `self`

`self` means: this concrete object.

```python
class Cow:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        return self.name
```

## Attribute

An attribute is data stored inside an object.

```python
cow.name
cow.legs
cow.speed
```

## Method

A method is a function inside a class.

```python
class Cow:
    def moo(self):
        return "moo"
```

Call it:

```python
cow = Cow("Bonya")
print(cow.moo())
```

## List of objects

```python
cows = [Cow("Bonya"), Cow("Shusha")]

for cow in cows:
    print(cow.moo())
```

## Object that stores objects

```python
class Farm:
    def __init__(self):
        self.cows = []

    def add_cow(self, cow):
        self.cows.append(cow)
```

## Inheritance

Inheritance means one class reuses code from another class.

```python
class Animal:
    def __init__(self, name, legs, speed):
        self.name = name
        self.legs = legs
        self.speed = speed

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, legs=4, speed=4)
```

## Abstract class

An abstract class is an unfinished parent class. It says: child classes must implement some methods.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
```

## Interface idea in Python

Python does not have Java-style interfaces. For beginners, use an abstract class as a contract.

```python
class Movable(ABC):
    @abstractmethod
    def move(self):
        pass
```
