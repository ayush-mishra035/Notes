class employee:
    start_time = "10am"
    end_time = "6am"

    def change_time(self,new_end_time):
        self.end_time = new_end_time
class Teacher(employee):
    def __init__(self,subject):
        self.subject = subject

class Admin(employee):
    def __init__(self,department):
        self.department = department

staff1 = Admin("accounts")
print(staff1.department , staff1.start_time , staff1.end_time)

t1 = Teacher("maths")
t1.change_time("5pm")
print(t1.subject , t1.start_time , t1.end_time)
