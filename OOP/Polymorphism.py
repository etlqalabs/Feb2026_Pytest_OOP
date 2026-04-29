'''
# 1 . Method overloading

class Addition:

    def add(self, a, b,c):
        return a + b+c

    def add(self, a, b):
        return a + b

obj = Addition()
ans1 = obj.add("one","two")
ans2 = obj.add(1,2)
print(ans1)
print(ans2)

'''

# Method overriding
class Vehicle:
    def start(self):
        print("Vehicle starts...")

    def stop(self):
        print("Vehicle stops...")

class Car(Vehicle):
    def start(self):
        print("Car starts")

    def honk(self):
        print("Car honking...")

# From Parent class
print("From parent class")
p = Vehicle()
p.start()
p.stop()


print("From Child class")
c = Car()
c.start()
c.stop()
c.honk()