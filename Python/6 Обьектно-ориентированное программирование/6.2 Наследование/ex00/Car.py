class Car:
    def __init__(self, brand=None):
        self._brand = brand

    def get_brand(self):
        return self._brand

    def stop(self):
        print('*The car stopped*')

    def drive(self):
        print('*The car started moving*')

class PassengerCar(Car):
    def __init__(self, brand=None, horsepower=0):
        super().__init__(brand)
        self._horsepower = horsepower

    @staticmethod
    def jump():
        print('The car jumped')

class Truck(Car):
    def __init__(self, brand=None):
        super().__init__(brand)
        self._occupancy = 0

    def submerge(self, count=0):
        self._occupancy += count

    def unload(self, count=0):
        self._occupancy -= count
    

#Main

car = Car('Volvo')
print(car.get_brand())
car.drive()
car.stop()
passenger_car = PassengerCar('Ford')
print(passenger_car.get_brand())
passenger_car.drive()
passenger_car.stop()
passenger_car.jump()
truck = Truck('Lada')
print(truck.get_brand())
print(truck._occupancy)
truck.submerge(100)
print(truck._occupancy)
truck.unload(50)
print(truck._occupancy)

print(isinstance(Car(), Car))
