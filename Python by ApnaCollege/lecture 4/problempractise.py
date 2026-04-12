class product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        product.count += 1

    def get_info(self):
        print(f"price pf {self.name}is rs.{self.price} ")

    @classmethod
    def get_count(cls):
        print(f"total product in store = {cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        print(f"discounted price ={price -(price*discount/100)}")

p1 = product("phone",10000)
p2 = product("laptop",50000)
p3 = product("tablet",20000) 

p1.calc_discount(p1.price,12)
p1.get_info()
p2.get_info()
p3.get_info()