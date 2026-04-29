class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner          # public
        self._balance = balance     # protected (convention)
        self.__pin = pin            # private (name mangling)

    def print_details(self):
        print("Inside Base Class:")
        print("Owner:", self.owner)
        print("Balance:", self._balance)
        print("PIN:", self.__pin)

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, pin, interest_rate):
        super().__init__(owner, balance, pin)
        self.interest_rate = interest_rate

    def access_parent_data(self):
        print("\nInside Child Class:")
        print("Owner:", self.owner)         # accessible
        print("Balance:", self._balance)    # accessible (protected)
        print("PIN:", self._BankAccount__pin)


sb = SavingsAccount("Hetu", 1000, 1234, 12)

print("Inside class...")
sb.print_details()

print("Inside subclass...")
sb.access_parent_data()

print(sb.owner)
print(sb._balance)
print(sb._BankAccount__pin)