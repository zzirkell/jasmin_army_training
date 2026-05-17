# Common Classes Pro Errors

## Calling property like a method

Wrong:

```python
cow.speed()
```

Correct:

```python
cow.speed
```

## Property returns itself forever

Wrong:

```python
@property
def speed(self):
    return self.speed
```

Correct:

```python
@property
def speed(self):
    return self._speed
```

## Static method has `self`

Wrong:

```python
@staticmethod
def add(self, a, b):
    return a + b
```

Correct:

```python
@staticmethod
def add(a, b):
    return a + b
```

## Thinking `Final` is strict runtime protection

`Final` is a hint. Python may still allow reassignment at runtime.
