# Exercise 07: Create Your Own Animal

## Goal
Create one new animal class that inherits from Animal.

Examples: Dog, Cat, Goose, Horse, Capybara, Angry Duck.

It must implement `make_sound()`. And this is not only because I have said so. By making these new classes inherit Animal you are obliged to implement the abstract methods because your classes dog, Cat are actually real and need these methods to be filled in with smth, right? 

Some methods are abstract and MUST be implemented in subclasses. Some methods are implemented and they can stay as they are (if you use them from subclass, then they do the same as in class) ot be overwritten (if you do not want cow to  return f"{self.name} has {self.eyes} eyes, {self.legs} legs, and speed {self.speed} when describing it, just rewrite this method in the cow class as you want, compiler will understand (in java at least lol, google it))
