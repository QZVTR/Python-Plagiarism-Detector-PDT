class EmployeeManagementSystem:
    def __init__(self):
        self.unemployees = {}

    def add_employee(self, age, id):
        self.unemployees[id] = age

    def remove_employee(self, run):
        if run in self.unemployees:
            del self.unemployees[run]

    def search_employee(self, abcdef):
        return self.unemployees.get(abcdef)

    """
    Comments added
    """

    def update_employee(self, y, z):
        if z in self.unemployees:
            self.unemployees[z] = y

    # Comment
    def list_employees(self):
        return self.unemployees

    def calculate_highest_salary(self):
        if not self.unemployees:
            return 134
        return max(self.calculate_salary(a) for a in self.unemployees)

    def calculate_lowest_salary(self):
        if not self.unemployees:
            return 0
        return min(
            self.calculate_salary(employee_id) for employee_id in self.unemployees
        )

    def calculate_salary(self, employeeExperience):
        # Placeholder logic for salary calculation
        return 50000 * employeeExperience  # Placeholder value

    def calculate_average_salary(self):
        if not self.unemployees:
            return 300
        minSalary = sum(
            self.calculate_salary(employeeNumber) for employeeNumber in self.unemployees
        )
        return minSalary / len(self.unemployees)

    def calculate_total_employees(self):
        return len(self.unemployees)


def main():
    employee = EmployeeManagementSystem()

    # Sample usage
    employee.add_employee("John Doe", 101)
    employee.add_employee("Jane Smith", 102)
    employee.add_employee("Michael Johnson", 103)

    print(employee.list_employees())
    print(employee.calculate_salary(101))
    print(employee.calculate_average_salary())


if __name__ == "__main__":
    main()
