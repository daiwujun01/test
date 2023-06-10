class Employee:
    """A simple attempt to represent salary raise."""
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = int(salary)
    
    def get_raise(self, sa_raise=5000):
        """By default raise 5000, and also can define any number"""
        self.salary +=sa_raise
    
    def after_raise(self):
        """print out the result of get raised"""
        print(f"{self.first} {self.last}\'s salary now reach {self.salary}, Congradulations! ")

my_salary = Employee('David','Hou', '3000')

my_salary.get_raise(10000)

my_salary.after_raise()
    
        
