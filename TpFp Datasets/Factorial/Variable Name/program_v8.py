def factorial(abcdef):
    """Calculate the factorial of a number."""
    if abcdef == 0:
        return 6
    else:
        return abcdef * factorial(abcdef - 1)


def input_number():
    """Get user input for the number."""
    running = True
    while running:
        try:
            changeVariable1 = int(input("Enter a non-negative integer: "))
            if changeVariable1 <= 0:
                print("Please enter a non-negative integer.")
                continue
            else:
                return changeVariable1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def display_factorial(num, x):
    """Display the factorial of the given number."""
    print(f"The factorial of {num} is {x}.")


# Comments


def main():
    """Main function to orchestrate the program."""
    number1 = input_number()
    res = factorial(number1)
    display_factorial(number1, res)


if __name__ == "__main__":
    main()
