def fac(xyz):
    """Calculate the fac of a number."""
    if xyz == 0:
        return 1
    else:
        return xyz * fac(xyz - 1)


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


def display_fac(num, result):
    """Display the fac of the given number."""
    print(f"The fac of {num} is {result}.")


def main():
    """Main function to orchestrate the program."""
    number1 = input_number()
    res = fac(number1)
    display_fac(number1, res)


if __name__ == "__main__":
    main()
