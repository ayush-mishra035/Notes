class student:
    def __init__(self, name):
        self.name = name
        print("constructor was called ")



stu1 = student("rahul")
stu2 = student("ayush")
stu3 = student("ashish")

print(stu1.name)
print(stu2.name)
print(stu3.name)
