
class Employee:
    def_increment = 0.1 #class variables
    emp_number = 0

    def __init__(self, first, last, salary): # Class Constructor
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + last + "@gmail.com"
        self.performance = 0 # instance variable

        Employee.emp_number += 1 

    def increment(self): # regular methods
        self.salary = self.salary * (1+(self.performance+Employee.def_increment/100))
    
    def up_rating(self):
        if (self.performance < 5):
            self.performance += 1
    
    def down_rating(self):
        if (self.performance >= 0):
            self.performance -= 1

    @staticmethod
    def employee_count(): # static method
        return Employee.emp_number

class Developer(Employee): # sub class
    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang
    
    @classmethod # class method
    def new_dev(cls, details):
        first, last, salary, prog_lang = details.split(" ")
        return cls(first, last, salary, prog_lang)

class Manager(Employee):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        self.employees = employees if employees != None else []
    def add_employees(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        # self.employees = self.employees.appned(emp) if emp not in self.employees else self.employees = self.employees
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    @classmethod
    def new_manager(cls, details):
        first, last, salary, employees = details.split(" ")
        return cls(first, last, salary, employees)


dev_1 = Developer.new_dev("Vishal Vennu 20000 Python")
manager_1 = Manager("Rakavee", "Anandan", 30000, dev_1)
print(manager_1.employees.email)
print(Employee.employee_count())