class Bankaccount:
    def __init__(self,name,balance):
        self.name = name #public attribute
        self.__balance = balance    #private attribute
    def get_balance(self):
        return self.__balance
    
    def set_balance(self , newbalance): # setter
        self.__balance = newbalance
acc1 = Bankaccount("Rahul kumar,100000")
print(acc1.name,acc1.balance)