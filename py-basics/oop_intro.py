# Define a class named 'Car'
class Car:
    # Class constructor (initializer)
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    # Method to start the car
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.year} {self.make} {self.model} is now running.")
        else:
            print("The car is already running.")

    # Method to stop the car
    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.year} {self.make} {self.model} has been stopped.")
        else:
            print("The car is already stopped.")

# Create instances (objects) of the 'Car' class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Tesla", "Model S", 2022)

# Accessing attributes and methods of objects
print(f"{car1.year} {car1.make} {car1.model}")
car1.start()
car1.stop()

print(f"{car2.year} {car2.make} {car2.model}")
car2.start()
car2.stop()
