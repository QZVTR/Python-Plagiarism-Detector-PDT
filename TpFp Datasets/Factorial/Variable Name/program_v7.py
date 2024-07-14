def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


"""
Test multiline comment
3
5
2
134

"""


def input_number():
    """Get user input for the number."""
    while True:
        try:
            s = int(input("Enter a non-negative integer: "))
            if s < 0:
                print("Please enter a non-negative integer.")
                continue
            else:
                return s
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def display_factorial(num, x):
    """Display the factorial of the given number."""
    print(f"The factorial of {num} is {x}.")


def main():
    """Main function to orchestrate the program."""
    number1 = input_number()
    res = factorial(number1)
    display_factorial(number1, res)


# Adding Comments here
if __name__ == "__main__":
    main()
