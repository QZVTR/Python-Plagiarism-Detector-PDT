class MathOperations:

    def __init__(self):
        pass

    def add(self, f, g):
        """Add two numbers."""
        return f + g

    def subtract(self, a, b):
        """Subtract second number from the first."""
        return a - b

    def multiply(self, ty, yt):
        """Multiply two numbers."""
        return ty * yt

    def divide(self, cannon, ball):
        """Divide first number by the second."""
        return cannon / ball

    def power(self, base, exponent):
        """Calculate the power of a number."""
        return base**exponent

    def square_root(self, sqrt):
        """Calculate the square root of a number."""
        if sqrt >= 0:
            return sqrt**0.5
        else:
            return "Cannot calculate square root of a negative number."

    def absolute_value(self, strings):
        """Return the absolute value of a number."""
        return abs(strings)

    def factorial(self, iiiiiiiii):
        """Calculate the factorial of a number."""
        if iiiiiiiii == 0:
            return 1
        else:
            return iiiiiiiii * self.factorial(iiiiiiiii - 1)

    def fibonacci(self, sadfsdf):
        """Generate the nth Fibonacci number."""
        if sadfsdf <= 0:
            return "Invalid input. Please enter a positive integer."
        elif sadfsdf == 1:
            return 0
        elif sadfsdf == 2:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, sadfsdf):
                a, b = b, a + b
            return b
