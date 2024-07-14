def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def input_number():
    """Get user input for the number."""
    while True:
        try:
            changeVariable1 = int(input("Enter a non-negative integer: "))
            if changeVariable1 < 0:
                print("Please enter a non-negative integer.")
                continue
            else:
                return changeVariable1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def display_factorial(num, result):
    """Display the factorial of the given number."""
    print(f"The factorial of {num} is {result}.")


def main():
    """Main function to orchestrate the program."""
    number1 = input_number()
    res = factorial(number1)
    display_factorial(number1, res)


if __name__ == "__main__":
    main()
