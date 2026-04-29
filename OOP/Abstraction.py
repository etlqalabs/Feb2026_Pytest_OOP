from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,noOfTyres):
        self.noOfTyres = noOfTyres

    @abstractmethod
    def start(self):
         pass

    @abstractmethod
    def honk(self):
        pass

    def stop(self):
         print("Vehicle stops..")

'''
# creating a object of abstrcat class
v = Vehicle(2)
v.stop()
v.start()
'''

class Car(Vehicle):
    def __init__(self):
        super().__init__(4)

    def start(self):
        print("Car starts...")

# Creating object of Car class which has implemeted now unimplemetd method from child

c = Car()
c.start()
c.stop()
