class Car:
    def __init__(self, make, model):
        self.fuel_level = 0 #private attribute

        #protected attributes
        self.make = make
        self.model = model
    

    #method to add fuel to the car object
    def addFuel(self, amount):
        if amount > 0:
            self.fuel_level += amount
        else:
            print("Not enough fuel")
    
    #method to drive th car
    #will deduct fuel from the car
    def drive(self, distance):
        fuel_needed = distance * 0.2
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            print(f"Drove {distance} km")
        else:
            print("Not enough fuel")

    #method to get fuel level
    def getFuelLevel(self):
        return self.fuel_level

#create an instance of the car
newCar = Car("Toyota", "Vios")

#add fuel to the created car instance
newCar.addFuel(50)

#drive the car
newCar.drive(100)

#print the remaining fuel level
print(f"Remaining fuel level: {newCar.getFuelLevel()} liters")

