class BankAccount :
    def __init__ (self, name: str, accNo: str, balance: float) :
        self.name = name
        self.accNo = accNo
        self.__balance = balance

    @property
    def balance (self) :
        return self.__balance  

    def __service_charge(self) :
        self.__balance *= 0.99  

    def deposit (self, amount: float) :
        if amount >= 0.0 :
            self.__balance += amount

        else:
            raise ValueError ("Amount is less than 0.0 $\n")
        
        self.__service_charge()

    def withdraw (self, amount: float) :
        if amount <= self.__balance :
            self.__balance -= amount

        else :
            raise ValueError ("Not enough balance, Gareeb!")
        
        self.__service_charge()
        

account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)