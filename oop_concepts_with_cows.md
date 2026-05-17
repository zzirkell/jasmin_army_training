# OOP Concepts Explained with Cows, Hearts, and Farms

The idea of this file:

> You already understand many OOP concepts from the farm exercises.  
> Now we only attach the official names to ideas you have already used.

OOP means **Object-Oriented Programming**.

Instead of writing one huge program, we create small “things” called **objects**.

A cow is a thing.

A farm is a thing.

A heart is a thing.

Each thing can have:

- data: what it knows
- behavior: what it can do

---

## 1. Class

A **class** is a blueprint.

It describes what kind of data and behavior an object should have.

Example:

```python
class Cow:
    pass
```

This means:

> There is a type of object called `Cow`.

But this does not create a real cow yet.

It only describes the idea of a cow.

### Cow explanation

A class is like saying:

> Every cow should have legs, eyes, speed, and the ability to moo.

---

## 2. Object

An **object** is one real thing created from a class.

Example:

```python
bonya = Cow()
shusha = Cow()
```

Now we have two cow objects.

`bonya` and `shusha` are both cows, but they are not the same object.

### Cow explanation

The class is the general idea:

> Cow

The objects are concrete cows:

> Bonya  
> Shusha

---

## 3. Constructor `__init__`

The constructor prepares a new object.

Example:

```python
class Cow:
    def __init__(self, name):
        self.name = name
```

When we write:

```python
bonya = Cow("Bonya")
```

Python creates a cow and stores `"Bonya"` inside it.

### Cow explanation

The constructor is like the moment when a new cow enters the farm and gets her personal data:

- name
- speed
- number of legs
- favorite food

---

## 4. Attribute

An **attribute** is data stored inside an object.

Example:

```python
class Cow:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
```

`name` and `speed` are attributes.

### Cow explanation

A cow can have attributes like:

```text
name = "Bonya"
legs = 4
eyes = 2
speed = 4
voice = "moo"
```

Attributes describe what the object knows about itself.

---

## 5. Method

A **method** is a function that belongs to an object.

Example:

```python
class Cow:
    def moo(self):
        return "moo"
```

Then:

```python
bonya = Cow()
print(bonya.moo())
```

### Cow explanation

A cow can do things:

- moo
- run
- eat
- sleep

In code, these actions are methods.

---

## 6. `self`

`self` means:

> this exact object.

Example:

```python
class Cow:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}"
```

If we write:

```python
bonya = Cow("Bonya")
shusha = Cow("Shusha")
```

Then:

```python
bonya.introduce()
```

uses Bonya’s name.

```python
shusha.introduce()
```

uses Shusha’s name.

### Cow explanation

`self` means:

> not any cow, this cow.

---

## 7. Encapsulation

**Encapsulation** means an object keeps its data and behavior together.

It also means we decide what other code should be allowed to use or change.

Example:

```python
class Cow:
    def __init__(self, name, speed):
        self.name = name
        self._speed = speed

    def get_speed(self):
        return self._speed
```

Here, the cow stores her speed inside herself.

Other code should ask the cow for her speed instead of changing it randomly.

### Cow explanation

Encapsulation is deciding:

> Which parts of the cow can the outside world touch?

Maybe the farm is allowed to ask:

```text
How fast can you run?
```

But maybe the farm should not be allowed to directly change:

```text
Your number of hearts is now 7.
```

A cow protects her important internal data.

Simple explanation:

> Encapsulation is “keep the cow’s private cow data inside the cow.”

---

## 8. Public and “Private” in Python

Python does not have strict private attributes like some other languages.

But Python uses naming conventions.

### Public

```python
self.name
```

This means:

> Other code can use this normally.

### Protected/private by convention

```python
self._speed
```

The underscore means:

> Please do not touch this directly unless you know what you are doing.

It is not strictly forbidden, but it is a warning.

### Cow explanation

Public:

```text
Cow name
Cow voice
```

Maybe okay to see.

Internal:

```text
Cow heart object
Cow internal health data
```

Maybe should not be changed directly from outside.

---

## 9. Getter

A **getter** is a method or property that lets other code read a value safely.

Example:

```python
class Cow:
    def __init__(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed
```

Or Python style:

```python
class Cow:
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed
```

Then:

```python
print(cow.speed)
```

### Cow explanation

Maybe the farm can ask:

> Cow, what is your speed?

But the farm cannot randomly set the speed to 999.

The cow allows reading the speed, but not changing it.

---

## 10. Setter

A **setter** controls how a value can be changed.

Example:

```python
class Cow:
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed < 0:
            print("Speed cannot be negative.")
            return

        self._speed = new_speed
```

### Cow explanation

Maybe speed can change, but only if the new speed is reasonable.

Allowed:

```text
speed = 5
```

Not allowed:

```text
speed = -100
```

A setter is like a small guard.

---

## 11. Inheritance

**Inheritance** means one class gets data and behavior from another class.

Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Cow(Animal):
    pass
```

Now Cow is an Animal.

### Cow explanation

A cow is an animal.

A sheep is an animal.

A dog is an animal.

So instead of repeating this in every class:

```text
name
speed
run()
sleep()
```

we can put common things into `Animal`.

Then Cow, Sheep, and Dog inherit from Animal.

---

## 12. Superclass / Parent Class

A **superclass** is the more general class.

Example:

```python
class Animal:
    pass
```

`Animal` is the superclass of `Cow`.

### Cow explanation

Animal is the general idea.

Cow is a specific type of animal.

```text
Animal
  Cow
  Sheep
  Dog
```

---

## 13. Subclass / Child Class

A **subclass** is the more specific class.

Example:

```python
class Cow(Animal):
    pass
```

`Cow` is a subclass of `Animal`.

### Cow explanation

A cow is a specific animal.

It has all general animal things, but it can also have cow-specific behavior:

```text
moo()
```

---

## 14. `super()`

`super()` calls code from the parent class.

Example:

```python
class Animal:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, 4)
```

### Cow explanation

Cow says:

> I am an Animal, so please let Animal prepare my common animal data.

Then Cow can add cow-specific things.

---

## 15. Method Overriding

**Overriding** means a child class provides its own version of a method.

Example:

```python
class Animal:
    def make_sound(self):
        return "some sound"

class Cow(Animal):
    def make_sound(self):
        return "moo"
```

### Cow explanation

Every animal can make a sound.

But the sound depends on the animal:

```text
Cow -> moo
Sheep -> baa
Dog -> woof
```

So each subclass overrides `make_sound()`.

---

## 16. Polymorphism

**Polymorphism** means we can use different objects through the same method name.

Example:

```python
animals = [Cow("Bonya"), Sheep("Dolly"), Dog("Milo")]

for animal in animals:
    print(animal.make_sound())
```

Python does not care whether the animal is a cow, sheep, or dog.

It only cares that the object has a method called `make_sound()`.

### Cow explanation

The farm says:

> All animals, make your sound!

Each animal responds in its own way:

```text
Bonya -> moo
Dolly -> baa
Milo -> woof
```

Same command, different behavior.

That is polymorphism.

---

## 17. Abstraction

**Abstraction** means we focus on what something should do, without caring about all details.

Example:

```python
class Animal:
    def make_sound(self):
        pass
```

This says:

> Every animal should make a sound.

But `Animal` itself does not know which sound.

Cow knows:

```python
def make_sound(self):
    return "moo"
```

Dog knows:

```python
def make_sound(self):
    return "woof"
```

### Cow explanation

A general animal is too abstract.

If someone asks:

> What sound does an animal make?

The answer is:

> It depends on the animal.

So `Animal` can define the idea, while Cow/Dog/Sheep provide the details.

---

## 18. Abstract Class

An **abstract class** is a class that should not be used directly.

It is used as a contract for child classes.

Example:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
```

Now every subclass must implement `make_sound()`.

### Cow explanation

We should not create a random generic animal:

```python
animal = Animal()
```

Because we do not know:

- its sound
- its real movement
- its special behavior

But we can create:

```python
cow = Cow("Bonya")
dog = Dog("Milo")
```

An abstract class says:

> If you want to be an animal, you must know how to make a sound.

---

## 19. Interface / Contract

Python does not have Java-style interfaces as a separate basic keyword.

For beginners, think of an interface as a **contract**.

Example contract:

> Every movable animal must have a `move()` method.

In Python, we can express this with an abstract class:

```python
from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self):
        pass
```

### Cow explanation

The summer animal camp wants all animals to move.

It does not care if they:

- run
- crawl
- fly
- swim

It only requires:

```text
You must have a move() method.
```

That is the contract.

---

## 20. Composition

**Composition** means one object contains another object.

Example:

```python
class Heart:
    def __init__(self, bpm):
        self.bpm = bpm

class Cow:
    def __init__(self, name):
        self.name = name
        self.heart = Heart(70)
```

The cow has a heart.

### Cow explanation

A cow is not a heart.

A cow has a heart.

This is not inheritance.

Wrong idea:

```text
Cow is a Heart
```

Correct idea:

```text
Cow has a Heart
```

This is composition.

---

## 21. Static Method

A **static method** belongs to a class, but it does not need object-specific data.

Example:

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

Usage:

```python
result = Calculator.add(3, 5)
```

No need to create this:

```python
calculator = Calculator()
```

### Cow explanation

A cow object needs personal data:

```text
Bonya has speed 4
Shusha has speed 5
```

But adding numbers is always the same:

```text
3 + 5 = 8
```

It does not depend on a specific calculator object.

That is why static methods are useful.

---

## 22. Class Variable

A **class variable** is shared by all objects of a class.

Example:

```python
class Cow:
    number_of_legs = 4
```

Every cow has 4 legs by default.

### Cow explanation

Bonya and Shusha can have different names.

But all normal cows have 4 legs.

So this can belong to the class:

```python
number_of_legs = 4
```

---

## 23. Instance Variable

An **instance variable** belongs to one specific object.

Example:

```python
class Cow:
    def __init__(self, name):
        self.name = name
```

Each cow has her own name.

### Cow explanation

Bonya’s name is Bonya.

Shusha’s name is Shusha.

So `name` should be an instance variable.

---

## 24. Constant / Final Idea

Python does not strongly enforce `final` values at runtime in the same simple way as some languages.

But we can use conventions and type hints.

Example:

```python
from typing import Final

COW_HEARTS: Final = 1
```

This means:

> This value should not be changed.

### Cow explanation

A cow normally has 1 heart.

That should not change during the cow’s lifetime.

But the heart’s BPM can change.

So:

```text
number of hearts = stable
heart bpm = changeable
```

---

## 25. Global Variable

A **global variable** is defined outside functions and classes.

Example:

```python
FARM_NAME = "Happy Cow Farm"
```

It can be used in many places.

### Cow explanation

The farm name might be known everywhere in the program.

But be careful: too many global variables make programs messy.

Usually, prefer storing data inside objects.

Good:

```python
farm.name
```

Risky if overused:

```python
global_farm_name
```

---

## 26. Summary Table

| Concept | Cow/Farm Meaning |
|---|---|
| Class | Blueprint for a cow |
| Object | Real cow, like Bonya |
| Attribute | Data: name, speed, legs |
| Method | Behavior: moo, run, eat |
| `self` | This exact cow |
| Constructor | Prepares a new cow |
| Encapsulation | Cow protects her internal data |
| Getter | Ask the cow for information |
| Setter | Safely change cow data |
| Inheritance | Cow is an Animal |
| Superclass | Animal |
| Subclass | Cow |
| Overriding | Cow has her own sound |
| Polymorphism | All animals make sounds differently |
| Abstraction | Animal defines idea, subclasses define details |
| Abstract class | Contract for real animals |
| Interface/contract | Must have a method like `move()` |
| Composition | Cow has a Heart |
| Static method | Calculator.add() does not need an object |
| Class variable | Shared data, like normal cow leg count |
| Instance variable | Personal data, like cow name |
| Final/constant | Should not change, like number of hearts |
| Global variable | Available outside classes/functions |

---

## 27. The Big OOP Idea

OOP is not mainly about syntax.

It is about organizing code around meaningful things.

In our farm world:

```text
Cow knows cow things.
Sheep knows sheep things.
Farm manages animals.
SummerAnimalCamp organizes shared activities.
Heart belongs to an animal.
Calculator does general calculations.
```

Good OOP means:

> Put the responsibility in the object where it naturally belongs.

A cow should know how to moo.

A farm should know which animals it has.

A calculator should know how to add numbers.

A heart should know its BPM.

That is the whole idea.
