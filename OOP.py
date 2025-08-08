# Assignment 1: Design Your Own Class

# Parent class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")


# Child class (Inheritance)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)  # Call parent constructor
        self.gpu = gpu

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU")

    def info(self):  # Polymorphism (method overriding)
        print(f"Gaming Phone - Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, GPU: {self.gpu}")


# Test
phone1 = Smartphone("Samsung", "Galaxy S24", 256)
phone1.info()
phone1.call("+123456789")

phone2 = GamingSmartphone("Asus", "ROG Phone 7", 512, "Adreno 740")
phone2.info()
phone2.play_game("Call of Duty")


# Activity 2: Polymorphism Challenge

class Car:
    def move(self):
        print("Driving")

class Plane:
    def move(self):
        print("Flying")

class Boat:
    def move(self):
        print("Sailing")


# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
