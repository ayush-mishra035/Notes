# Multiple Inheritance

class teacher:
    def __init__(self,salary):
        self.salary = salary

class student:
    def __init__(self,gpa):
        self.gpa =gpa

class ta(teacher, student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary)
        self.gpa = gpa
        self.name = name

ta1 = ta(25000, 8.5, "Rahul")
print(ta1.name, ta1.salary, ta1.gpa)