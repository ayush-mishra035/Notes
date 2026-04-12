# mutiple level inheritance
class employee:

    start_time = "10am"
    end_time = "6pm"

class adminstaff(employee):
    def __init__(self,role):
        self.role = role

class accountant(adminstaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary = salary
acc1 = accountant(250000, "ca")
print(acc1.salary , acc1.role , acc1.start_time , acc1.end_time)