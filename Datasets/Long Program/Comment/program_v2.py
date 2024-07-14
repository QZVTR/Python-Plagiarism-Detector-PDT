import os
import json


class BankingSystem:
    # Comment 1
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance):
        account_number = len(self.accounts) + 1
        self.accounts[account_number] = {
            "name": name,
            "balance": balance,
            "transactions": [],
        }
        return account_number

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            self.accounts[account_number]["transactions"].append(f"Deposited ${amount}")

    def withdraw(self, account_number, amount):
        if (
            account_number in self.accounts
            and self.accounts[account_number]["balance"] >= amount
        ):
            self.accounts[account_number]["balance"] -= amount
            self.accounts[account_number]["transactions"].append(f"Withdrew ${amount}")

    def transfer(self, sender_account, receiver_account, amount):
        if (
            sender_account in self.accounts
            and receiver_account in self.accounts
            and self.accounts[sender_account]["balance"] >= amount
        ):
            self.accounts[sender_account]["balance"] -= amount
            self.accounts[receiver_account]["balance"] += amount
            self.accounts[sender_account]["transactions"].append(
                f"Transferred ${amount} to account {receiver_account}"
            )
            self.accounts[receiver_account]["transactions"].append(
                f"Received ${amount} from account {sender_account}"
            )

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]["balance"]
        else:
            return "Account not found"

    def get_transaction_history(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]["transactions"]
        else:
            return "Account not found"

    def calculate_interest(self, account_number):
        if account_number in self.accounts:
            # Placeholder logic for interest calculation
            return 0.05 * self.accounts[account_number]["balance"]  # 5% interest rate
        else:
            return "Account not found"

    def calculate_total_accounts(self):
        return len(self.accounts)


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, employee_id):
        self.employees[employee_id] = name

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]

    def search_employee(self, employee_id):
        return self.employees.get(employee_id)

    def update_employee(self, name, employee_id):
        if employee_id in self.employees:
            self.employees[employee_id] = name

    def list_employees(self):
        return self.employees

    def calculate_salary(self, employee_id):
        # Placeholder logic for salary calculation
        return 50000  # Placeholder value

    def calculate_average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(
            self.calculate_salary(employee_id) for employee_id in self.employees
        )
        return total_salary / len(self.employees)

    def calculate_total_employees(self):
        return len(self.employees)

    def calculate_highest_salary(self):
        if not self.employees:
            return 0
        return max(self.calculate_salary(employee_id) for employee_id in self.employees)

    def calculate_lowest_salary(self):
        if not self.employees:
            return 0
        return min(self.calculate_salary(employee_id) for employee_id in self.employees)


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
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Please enter a non-negative integer.")
                continue
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def display_factorial(number, result):
    """Display the factorial of the given number."""
    print(f"The factorial of {number} is {result}.")


class MathOperations:

    def __init__(self):
        pass

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
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero."

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


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.assigned_projects = []

    def assign_project(self, project):
        self.assigned_projects.append(project)

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}"


class Project:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"Project ID: {self.project_id}, Name: {self.name}"


class Task:
    def __init__(self, task_id, description, status="To Do"):
        self.task_id = task_id
        self.description = description
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}, Status: {self.status}"


class ProjectManager:
    def __init__(self):
        self.users = {}
        self.projects = {}
        self.tasks = {}

    def create_user(self, user_id, name):
        user = User(user_id, name)
        self.users[user_id] = user
        return user

    def create_project(self, project_id, name):
        project = Project(project_id, name)
        self.projects[project_id] = project
        return project

    def create_task(self, task_id, description, project_id):
        task = Task(task_id, description)
        self.tasks[task_id] = task
        if project_id in self.projects:
            self.projects[project_id].add_task(task)
        return task

    def assign_project_to_user(self, project_id, user_id):
        if user_id in self.users and project_id in self.projects:
            self.users[user_id].assign_project(self.projects[project_id])

    def __str__(self):
        users_str = "\n".join(str(user) for user in self.users.values())
        projects_str = "\n".join(str(project) for project in self.projects.values())
        tasks_str = "\n".join(str(task) for task in self.tasks.values())
        return (
            f"Users:\n{users_str}\n\nProjects:\n{projects_str}\n\nTasks:\n{tasks_str}"
        )


class StudentRecord:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_no):
        self.students[roll_no] = name

    def remove_student(self, roll_no):
        if roll_no in self.students:
            del self.students[roll_no]

    def search_student(self, roll_no):
        return self.students.get(roll_no)
