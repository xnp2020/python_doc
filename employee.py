class Employee:
    """年薪增加"""

    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.full_name = f"{self.first_name} {self.last_name}"

    def give_raise(self,add_salary=5000):
        self.salary += add_salary

    def get_salary(self):
        
        return f"{self.full_name.title()} salary is {self.salary}"


wan = Employee("wan","ting",10000)
wan.get_salary()
wan.give_raise(15000)
wan.get_salary()
