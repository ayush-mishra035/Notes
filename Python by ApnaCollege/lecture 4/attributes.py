class student:
    college_name = "ABC college" # class
    PI = 3.14 # class attribute

    def __init__(self, name, cgpa):
        self.name = name   # instaqnce attribute
        self.cgpa = cgpa   # instance attribute

        stu1 = student("rahul",9.2)

        print(stu1.name)
        print(student.college_name)