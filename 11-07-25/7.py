class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_net_salary(self):
        hra = 0.20 * self.basic_salary
        da = 0.10 * self.basic_salary
        net_salary = self.basic_salary + hra + da
        return net_salary


emp = Employee("John", 50000)
print("Net Salary of", emp.name, "is", emp.calculate_net_salary())
