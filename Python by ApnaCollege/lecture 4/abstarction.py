# abstraction 

from abc import ABC

class ANIMAL(ABC):
    def make_sound():
        pass
class DOG(ANIMAL):
    def make_sound():
        print("Woof")

class CAT(ANIMAL):
    def make_sound(self):
        print("Meow")

class LION(ANIMAL):
    def make_sound(self):
        print("Roar")

lion = LION()
lion.make_sound()

cat = CAT()
cat.make_sound()