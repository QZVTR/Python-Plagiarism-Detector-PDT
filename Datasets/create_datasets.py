import os
import random
import re


def generate_program(iteration):
    program_name = f"program_v{iteration}.py"
    with open(program_name, "w") as file:
        file.write("class MathOperations:\n\n")
        file.write("\tdef __init__(self):\n")
        file.write("\t\tpass\n\n")
        file.write("\tdef add(self, a, b):\n")
        file.write('\t\t"""Add two numbers."""\n')
        file.write("\t\treturn a + b\n\n")
        file.write("\tdef subtract(self, a, b):\n")
        file.write('\t\t"""Subtract second number from the first."""\n')
        file.write("\t\treturn a - b\n\n")
        file.write("\tdef multiply(self, a, b):\n")
        file.write('\t\t"""Multiply two numbers."""\n')
        file.write("\t\treturn a * b\n\n")
        file.write("\tdef divide(self, a, b):\n")
        file.write('\t\t"""Divide first number by the second."""\n')
        file.write("\t\tif b != 0:\n")
        file.write("\t\t\treturn a / b\n")
        file.write("\t\telse:\n")
        file.write('\t\t\treturn "Cannot divide by zero."\n\n')
        file.write("\tdef power(self, base, exponent):\n")
        file.write('\t\t"""Calculate the power of a number."""\n')
        file.write("\t\treturn base ** exponent\n\n")
        file.write("\tdef square_root(self, num):\n")
        file.write('\t\t"""Calculate the square root of a number."""\n')
        file.write("\t\tif num >= 0:\n")
        file.write("\t\t\treturn num ** 0.5\n")
        file.write("\t\telse:\n")
        file.write(
            '\t\t\treturn "Cannot calculate square root of a negative number."\n\n'
        )
        file.write("\tdef absolute_value(self, num):\n")
        file.write('\t\t"""Return the absolute value of a number."""\n')
        file.write("\t\treturn abs(num)\n\n")
        file.write("\tdef factorial(self, n):\n")
        file.write('\t\t"""Calculate the factorial of a number."""\n')
        file.write("\t\tif n == 0:\n")
        file.write("\t\t\treturn 1\n")
        file.write("\t\telse:\n")
        file.write("\t\t\treturn n * self.factorial(n - 1)\n\n")
        file.write("\tdef fibonacci(self, n):\n")
        file.write('\t\t"""Generate the nth Fibonacci number."""\n')
        file.write("\t\tif n <= 0:\n")
        file.write('\t\t\treturn "Invalid input. Please enter a positive integer."\n')
        file.write("\t\telif n == 1:\n")
        file.write("\t\t\treturn 0\n")
        file.write("\t\telif n == 2:\n")
        file.write("\t\t\treturn 1\n")
        file.write("\t\telse:\n")
        file.write("\t\t\ta, b = 0, 1\n")
        file.write("\t\t\tfor _ in range(2, n):\n")
        file.write("\t\t\t\ta, b = b, a + b\n")
        file.write("\t\t\treturn b\n\n")


def modify_program(iteration):
    if iteration == 0:
        generate_program(1)
        return

    with open(f"program_v{iteration}.py", "r") as original_file:
        lines = original_file.readlines()

    # Make slight modifications
    modification = random.choice(["comment"])  # ,"reorder" "rename"])
    modified_lines = lines[:]
    if modification == "comment":
        line_number = random.randint(1, len(lines) - 1)
        modified_lines.insert(
            line_number,
            "# This is a new comment added in iteration {}\n".format(iteration),
        )
    elif modification == "reorder":
        # Preserve import statements and function definitions
        essential_lines = [
            line for line in modified_lines if line.startswith(("import", "def"))
        ]
        modified_lines = [
            line for line in modified_lines if line not in essential_lines
        ]
        random.shuffle(modified_lines)
        modified_lines = essential_lines + modified_lines
    elif modification == "rename":
        modified_lines = [rename_variables(line, iteration) for line in modified_lines]

    modified_program_name = f"program_v{iteration + 1}.py"
    with open(modified_program_name, "w") as modified_file:
        modified_file.writelines(modified_lines)


def rename_variables(line, iteration):
    # This function will replace variable names with new names
    # based on the iteration number
    # Variable assignments with specific patterns are targeted for renaming
    # For simplicity, this example changes 'num' to 'changeVariable{iteration}'
    pattern = r"(\bnum\b)(?=\s*=\s*int\s*\()"
    replacement = f"changeVariable{iteration}"
    return re.sub(pattern, replacement, line)


# Start modification process
for i in range(0, 11):
    modify_program(i)

    # Execute the modified program
    # os.system(f"python program_v{i}.py")
