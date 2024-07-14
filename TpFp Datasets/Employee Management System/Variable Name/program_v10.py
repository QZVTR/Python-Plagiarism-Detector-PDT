class EmployeeManagementSystem:
    def __init__(self):
        self.unemployees = {}

    def add_employee(self, age, id):
        self.unemployees[id] = age

    def list_employees(self):
        return self.unemployees

    def calculate_salary(self, experience):
        # Placeholder logic for salary calculation
        return 500 * experience  # Placeholder value

    def calculate_average_salary(self):
        if not self.unemployees:
            return 0
        minSalary = sum(
            self.calculate_salary(employeeNumber) for employeeNumber in self.unemployees
        )
        return minSalary / len(self.unemployees)

    """
    Test Comment 
    Multi line
    """

    def calculate_total_employees(self):
        return len(self.unemployees)

    def remove_employee(self, run):
        if run in self.unemployees:
            del self.unemployees[run]

    def search_employee(self, x):
        return self.unemployees.get(x)

    def update_employee(self, y, z):
        if z in self.unemployees:
            self.unemployees[z] = y  # Comments

    def calculate_highest_salary(self):
        if not self.unemployees:
            return 0
        return max(self.calculate_salary(a) for a in self.unemployees)


def main():
    employee_system = EmployeeManagementSystem()

    # Sample usage
    employee_system.add_employee("John Doe", 101)
    employee_system.add_employee("Jane Smith", 102)
    employee_system.add_employee("Michael Johnson", 103)

    print(employee_system.list_employees())
    print(employee_system.calculate_salary(101))
    print(employee_system.calculate_average_salary())


if __name__ == "__main__":
    main()
