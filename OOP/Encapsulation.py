class BankAccount:
    def __init__(self,owner,balance,pin):
        self.owner = owner
        self._balance = balance
        self.__pin = pin

    def print_pin(self):
        print(self.owner)
        print(self._balance)
        print(self.__pin)

class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,pin,interest_rate):
        super().__init__(owner,balance,pin)
        self.interest_rate = interest_rate

class outside:
    sb = SavingsAccount("Hetu",1000,1234,12)

    '''
    print(sb.owner)
    print(sb._balance)
    print(sb.interest_rate)
    '''









