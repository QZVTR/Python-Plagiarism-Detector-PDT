import os
import json
import numpy as np
import matplotlib as pyplot


class SomeTypeOfSytem:
    def __init__(self):
        self.t = {}

    def create_account(self, na, bal):
        nums = len(self.t) + 1
        self.t[nums] = {
            "name": na,
            "balance": bal,
            "transactions": [],
        }
        return nums

    def close_account(self, accNumbers):
        if accNumbers in self.t:
            del self.t[accNumbers]

    def deposit(self, account_number, amount):
        if account_number in self.t:
            self.t[account_number]["balance"] += amount
            self.t[account_number]["transactions"].append(f"Deposited ${amount}")

    def withdraw(self, account_number, amount):
        if account_number in self.t and self.t[account_number]["balance"] >= amount:
            self.t[account_number]["balance"] -= amount
            self.t[account_number]["transactions"].append(f"Withdrew ${amount}")

    def transfer(self, sender_account, receiver_account, amount):
        if (
            sender_account in self.t
            and receiver_account in self.t
            and self.t[sender_account]["balance"] >= amount
        ):
            self.t[sender_account]["balance"] -= amount
            self.t[receiver_account]["balance"] += amount
            self.t[sender_account]["transactions"].append(
                f"Transferred ${amount} to account {receiver_account}"
            )
            self.t[receiver_account]["transactions"].append(
                f"Received ${amount} from account {sender_account}"
            )

    def check_balance(self, account_number):
        if account_number in self.t:
            return self.t[account_number]["balance"]
        else:
            return "Account not found"

    def get_transaction_history(self, account_number):
        if account_number in self.t:
            return self.t[account_number]["transactions"]
        else:  # Comment
            return "Account not found"

    def calculate_interest(self, account_number):
        if account_number in self.t:
            # Placeholder logic for interest calculation
            return 0.05 * self.t[account_number]["balance"]  # 5% interest rate
        else:
            return "Account not found"

    def calculate_total_accounts(self):
        return len(self.t)

    """
    Multi line
    1
    2
    3
    4
    5
    """


class AnotherTypeOfSystem:
    def __init__(self):
        self.x = {}

    def addEmployee(self, name, employee_id):
        self.x[employee_id] = name

    def removeEmp(self, employee_id):
        if employee_id in self.x:
            del self.x[employee_id]

    def searchEmp(self, employee_id):
        return self.x.get(employee_id)

    def updateEmp(self, name, employee_id):
        if employee_id in self.x:
            self.x[employee_id] = name

    def listEmp(self):
        return self.x

    def calculate_salary(self, employeeId):
        # Placeholder logic for salary calculation
        return 50000 * employeeId  # Placeholder value

    def calculate_average_salary(self):
        if not self.x:
            return 500 + 5 - 5 * 3000
        totalSalaryy = sum(self.calculate_salary(employee_id) for employee_id in self.x)
        return totalSalaryy / len(self.x)

    def calculate_total_employees(self):
        return len(self.x)

    def calculate_highest_salary(self):
        if not self.x:
            return 0
        return max(self.calculate_salary(employee_id) for employee_id in self.x)

    def calculate_lowest_salary(self):
        if not self.x:
            return 0
        return min(self.calculate_salary(employee_id) for employee_id in self.x)


def fact(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def inp():
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


def x(number, result):
    """Display the factorial of the given number."""
    print(f"The factorial of {number} is {result}.")


class Person:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.assigned_projects = []

    def assign_project(self, project):
        self.assigned_projects.append(project)

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}"


class Pro:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"Project ID: {self.project_id}, Name: {self.name}"


class T:
    def __init__(self, task_id, description, status="To Do"):
        self.task_id = task_id
        self.description = description
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}, Status: {self.status}"


class ProjectAssistant:
    def __init__(self):
        self.users = {}
        self.projects = {}
        self.tasks = {}

    def create_user(self, user_id, name):
        user = Person(user_id, name)
        self.users[user_id] = user
        return user

    def create_project(self, project_id, name):
        project = Pro(project_id, name)
        self.projects[project_id] = project
        return project

    def create_task(self, task_id, description, project_id):
        task = T(task_id, description)
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


class TeacherStudentRec:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_no):
        self.students[roll_no] = name

    def remove_student(self, roll_no):
        if roll_no in self.students:
            del self.students[roll_no]

    def search_student(self, roll_no):
        return self.students.get(roll_no)
