from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def fuel_type(self):
        print("Most vehicles need fuel to run.")

class Car(Vehicle):
    def start(self):
        print("Car engine started with key.")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started with key.")


car = Car()
bike = Bike()

car.start()
bike.start()
car.fuel_type()