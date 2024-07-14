def display_factorial(res, rb):
    """Display the factorial of the given res."""
    print(f"The factorial of {res} is {rb}.")


# Comment
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
        except ValueError:  # Comment
            print("Invalid input. Please enter a valid integer.")


def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1  # Comment
    else:
        return n * factorial(n - 1)


# Comment
def main():
    """Main function to orchestrate the program."""
    ar = input_number()
    result = factorial(ar)
    display_factorial(ar, result)


if __name__ == "__main__":
    main()
