class MathOps:

    def __init__(self):
        pass

    def add(self, f, g):
        """Add two numbers."""
        return f + g

    def subtra(self, a, b):
        """Subtract second number from the first."""
        return a - b

    def muly(self, ty, yt):
        """Multiply two numbers."""
        return ty * yt

    def ide(self, cannon, ball):
        """Divide first number by the second."""
        return cannon / ball

    """
    Comment
    1
    2
    3
    4
    5
    """

    def por(self, base, exponent):
        """Calculate the power of a number."""
        return base**exponent

    def sqot(self, sqrt):
        """Calculate the square root of a number."""
        if sqrt >= 0:
            return sqrt**0.5
        else:
            return "Cannot calculate square root of a negative number."
