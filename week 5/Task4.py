class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary # Private attribute convention

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    # Overriding get_role
    def get_role(self):
        return "Manager"

    # New method specific to Manager
    def get_bonus(self):
        return self.bonus

def print_employee_details(employees):
    print(f"{'Name':<10} | {'Role':<10} | {'Salary'}")
    print("-" * 35)
    for emp in employees:
        # Polymorphism in action: calling the same methods on different object types
        print(f"{emp.name:<10} | {emp.get_role():<10} | ${emp.get_salary()}")

if __name__ == "__main__":
    staff = [
        Employee("Sarah", 50000),
        Manager("Mike", 80000, 5000),
        Employee("Tom", 52000)
    ]
    
    print_employee_details(staff)