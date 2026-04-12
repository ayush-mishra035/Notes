class laptop:
    storage_type = "ssd"

    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage

    def get_info(self):
        print(f"laptop has{self.ram}ram & {self.storage}{self.storage_type}")

l1=laptop("16gb","512gb")
l2=laptop("8gb","256gb")