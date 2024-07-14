class MathOperations:

    def __init__(self):
        self.x = 0
        self.y = 1
        pass

    def add(self, f, g):
        """Add two numbers."""
        return f + g

    def sub(self, a, b):
        """Subtract second number from the first."""
        return a - b

    def mult(self, x, y):
        """Multiply two numbers."""
        return x * y  # Comment

    def divide(self, cannon, ball):
        """Divide first number by the second."""
        return cannon / ball

    def power(self, base, exponent):
        """Calculate the power of a number."""
        return base**exponent  # Comment

    def squareRoot(self, sqrt):
        """Calculate the square root of a number."""
        if sqrt >= 0:
            return sqrt**0.5
        else:
            return "Cannot calculate square root of a negative number."
