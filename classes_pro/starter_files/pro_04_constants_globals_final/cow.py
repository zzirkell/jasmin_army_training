from constants import HEART_COUNT, DEFAULT_COW_SPEED

class Cow:
    def __init__(self, name):
        self.name = name
        self.heart_count = HEART_COUNT
        self.speed = DEFAULT_COW_SPEED

    def describe(self):
        return f"{self.name} has {self.heart_count} heart and speed {self.speed}."
