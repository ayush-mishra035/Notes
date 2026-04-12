# duck typing
class Duck:
    def fly(self):
        print("Duck is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def make_fly(obj):
    obj.fly()

duck = Duck()
airplane = Airplane()

make_fly(duck)
make_fly(airplane)