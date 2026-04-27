class Vehicle:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand
    def start_engine(self):
        print(f"{self.model} {self.brand} started..")
    def stop_engine(self):
        print(f"{self.model} {self.brand} stoped..")


class Bike(Vehicle):
    def __init__(self, model,brand):
        super().__init__(model,brand)
    def apply_break(self):
        print(f"{self.model} {self.brand} is applying break")


class Car(Vehicle):
    def __init__(self, model, brand,fuel_type):
        super().__init__(model,brand)
        self.fuel_type = fuel_type
    def honk(self):
        print(f"{self.model} {self.brand} is honking.. beep beep.. and also having {self.fuel_type} type")

class ElectricCar(Car,Bike):
    def __init__(self, model, brand,fuel_type,battery_capacity):
        super().__init__(model,brand,fuel_type)
        self.battery_capacity = battery_capacity
    def charge(self):
        print(f"{self.model} {self.brand} is charging...")


# Object creation of parent class
v = Vehicle("Honda","Honda civic")
'''
print("Methods from Vehicle class")
v.start_engine()
v.stop_engine()
'''

# Car class object creation
c = Car("Honda","Honda civic","Petrol")
'''
print("Methods from Car class")
c.start_engine()
c.stop_engine()
c.honk()
'''

# Super child to Vehicle class
ec = ElectricCar("Tesla","ModelS","Electric",100)
print("Methods from Electric Car class")
ec.start_engine()
ec.stop_engine()
ec.honk()
ec.charge()
ec.apply_break()


