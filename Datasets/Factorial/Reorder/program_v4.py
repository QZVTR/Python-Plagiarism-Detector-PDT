def display_factorial(number, result):
    """Display the factorial of the given number."""
    print(f"The factorial of {number} is {result}.")


def input_number():
    """Get user input for the number."""
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Please enter a non-negative integer.")
                continue
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    """Main function to orchestrate the program."""
    number = input_number()
    result = factorial(number)
    display_factorial(number, result)


def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    main()
