class laptop:
    storage_type = "ssd"

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_info(self):   # instance parameter beacuse using of self 
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Storage Type: {laptop.storage_type}"
laptop1 = laptop("dell", "inspiron", 50000)
laptop2 = laptop("hp", "pavilion", 60000)