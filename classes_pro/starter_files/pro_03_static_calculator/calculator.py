class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return None
        else:
            return a / b
    # TODO: add @staticmethod methods add, subtract, multiply, divide
    # If divide by zero, return None.
    pass
