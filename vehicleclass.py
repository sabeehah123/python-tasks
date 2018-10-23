class vehicle():
    def __init__(self,name):
        self.name=name
        print("Vehicle name: ", self.name)


    def wheels(self, number):
        self.number=number
        print("Number of Wheels: " , self.number)
        return self

    def colour(self,colour):
        self.colour=colour
        print("Vehicle colour: " , self.colour)
        return self


class car(vehicle):
    pass

class bike(vehicle):
    pass

class bus(vehicle):
    pass

class truck(vehicle):
    pass

car1=car("Car").wheels(4).colour("red")
print("\n")
bike1=bike("Motorbike").wheels(2).colour("blue")
print("\n")
bus1=bus("Bus").wheels(4).colour("red")
print("\n")
truck1=truck("Truck").wheels(4).colour("black")
print("\n")

class garage():
    vehicles=[]
    def addvehicle(self,vehicle1):
        self.vehicles.append(vehicle1)

garage=garage()
garage.addvehicle(car1)
garage.addvehicle(bike1)
garage.addvehicle(bus1)
garage.addvehicle(truck1)

print(garage.vehicles)

for Vehicle in garage.vehicles:
    print(isinstance(Vehicle, vehicle))