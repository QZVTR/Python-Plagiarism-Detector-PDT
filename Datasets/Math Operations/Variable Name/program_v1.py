class MathOperations:

    def __init__(self):
        pass

    """def testOps(self, x, y):
        res = x <= y
        a = 55 * 3
        b = 42 * 3
        return b == a"""

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract second number from the first."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide first number by the second."""
        return a / b

    def power(self, base, exponent):
        """Calculate the power of a number."""
        return base**exponent

    def square_root(self, num):
        """Calculate the square root of a number."""
        if num >= 0:
            return num**0.5
        else:
            return "Cannot calculate square root of a negative number."

    def absolute_value(self, num):
        """Return the absolute value of a number."""
        return abs(num)

    def factorial(self, n):
        """Calculate the factorial of a number."""
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def fibonacci(self, n):
        """Generate the nth Fibonacci number."""
        if n <= 0:
            return "Invalid input. Please enter a positive integer."
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n):
                a, b = b, a + b
            return b
