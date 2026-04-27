# Print 1 to 5
'''
# procedural way

print(1)
print(2)
print(3)
print(4)
print(5)



# Functional way
def print_num(number):
    for i in range(1,number+1):
        print(i)

print_num(5)



# OOP way
class PrintClass:
    def print_num(self,number):
        for i in range(1, number + 1):
            print(i)

obj1 = PrintClass()
obj1.print_num(10)

'''


# Real world example of a class and objects

'''
# Way 1
class MathsOperations:
    def __init__(self):
        print("I am a default constrcutor..")


    def add_numbers(self,num1,num2):
        return num1+num2

    def sub_numbers(self,num1,num2):
        return num1-num2

    def multi_numbers(self,num1,num2):
        return num1*num2

    def divide_numbers(self,num1,num2):
        return num1/num2

op1 = MathsOperations()
sum = op1.add_numbers(20,10)
print(sum)
sub = op1.sub_numbers(20,10)
print(sub)
product = op1.multi_numbers(20,10)
print(product)
division = op1.divide_numbers(20,10)
print(division)
'''

# Way 2 - intiate variables in the constructor
class MathsOperationsUsingParametrizedConstructor:
    def __init__(self,num1,num2):
        print("I am a parameterized constrcutor..")
        self.num1 = num1
        self.num2 = num2


    def add_numbers(self):
        return self.num1+self.num2

    def sub_numbers(self):
        return self.num1-self.num2

    def multi_numbers(self):
        return self.num1*self.num2

    def divide_numbers(self):
        return self.num1/self.num2

op1 = MathsOperationsUsingParametrizedConstructor(20,10)
sum = op1.add_numbers()
print(sum)
sub = op1.sub_numbers()
print(sub)
product = op1.multi_numbers()
print(product)
division = op1.divide_numbers()
print(division)

op2 = MathsOperationsUsingParametrizedConstructor(50,10)
sum = op2.add_numbers()
print(sum)
sub = op2.sub_numbers()
print(sub)
product = op2.multi_numbers()
print(product)
division = op2.divide_numbers()
print(division)

# get me the address of the objects created

print(hex(id(op1)))
print(hex(id(op2)))




