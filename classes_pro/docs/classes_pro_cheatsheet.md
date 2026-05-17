# Classes Pro Cheatsheet

## Getter with `@property`

```python
class Cow:
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed
```

Use it like an attribute:

```python
print(cow.speed)
```

## Setter with validation

```python
class Heart:
    def __init__(self, heartbeat):
        self.heartbeat = heartbeat

    @property
    def heartbeat(self):
        return self._heartbeat

    @heartbeat.setter
    def heartbeat(self, value):
        if value <= 0:
            raise ValueError("Heartbeat must be positive.")
        self._heartbeat = value
```

## Static method

Use static methods when the method does not need object-specific data.

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

```python
Calculator.add(3, 5)
```

## `Final`

```python
from typing import Final

HEART_COUNT: Final = 1
```

`Final` is mostly a hint for tools and humans. Python usually does not enforce it at runtime.

## Global variables

A global variable is outside functions/classes.

```python
DEFAULT_COW_SPEED = 4
```

Use globals mostly for constants. Avoid changing global variables from many places.

## Private/public in Python

```python
self.name      # public
self._speed    # internal by convention
self.__secret  # name-mangled, but still not truly private like Java
```
