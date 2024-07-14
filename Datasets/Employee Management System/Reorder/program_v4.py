class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def update_employee(self, name, employee_id):
        if employee_id in self.employees:
            self.employees[employee_id] = name

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]

    def search_employee(self, employee_id):
        return self.employees.get(employee_id)

    def list_employees(self):
        return self.employees

    def calculate_total_employees(self):
        return len(self.employees)

    def calculate_salary(self, employee_id):
        # Placeholder logic for salary calculation
        return 50000 * employee_id  # Placeholder value

    def calculate_average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(
            self.calculate_salary(employee_id) for employee_id in self.employees
        )
        return total_salary / len(self.employees)

    def calculate_highest_salary(self):
        if not self.employees:
            return 0
        return max(self.calculate_salary(employee_id) for employee_id in self.employees)

    def calculate_lowest_salary(self):
        if not self.employees:
            return 0
        return min(self.calculate_salary(employee_id) for employee_id in self.employees)

    def add_employee(self, name, employee_id):
        self.employees[employee_id] = name


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
