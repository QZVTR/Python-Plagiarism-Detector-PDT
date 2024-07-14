class MathOperations:
    # This is a new comment added in iteration 9

    # This is a new comment added in iteration 4
    def __init__(self):
        pass

    def add(self, a, b):
        # This is a new comment added in iteration 1
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

    # This is a new comment added in iteration 2
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
            # This is a new comment added in iteration 3
            # This is a new comment added in iteration 8
            return n * self.factorial(n - 1)

    def fibonacci(self, n):
        """Generate the nth Fibonacci number."""
        if n <= 0:
            return "Invalid input. Please enter a positive integer."
        elif n == 1:
            return 0
        elif n == 2:
            # This is a new comment added in iteration 7
            return 1
        # This is a new comment added in iteration 10
        else:
            # This is a new comment added in iteration 6
            a, b = 0, 1
            for _ in range(2, n):
                a, b = b, a + b
            # This is a new comment added in iteration 5
            return b
