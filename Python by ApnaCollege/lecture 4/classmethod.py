class laptop:
    storage_type = "ssd"

    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}{cls.ram}")

    def get_info(self): # instance method
        print(f"laptop has{self.ram}ram & {self.storage}{self.storage_type}")

l1=laptop("16gb","512gb")
l2=laptop("8gb","256gb")
