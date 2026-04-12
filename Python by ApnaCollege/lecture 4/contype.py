class student:
    def __init__(self, name, cgpa):  # parameterized constructor
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa
    
stu1 = student("rahul", 8.5)
stu2 = student("ayush", 9.0)
stu3 = student("ashish", 7.5)

print(stu1.name, stu1.cgpa)
print(stu2.name, stu2.cgpa)     
print(stu3.name, stu3.cgpa) 