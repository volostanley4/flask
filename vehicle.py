# Create a small vehicle management system using inheritance. Start by creating a parent class called Vehicle. The Vehicle class should have three attributes: brand, model, and year. It should have a display_info() method that prints the vehicle's basic information. Add a start() method that prints a simple message saying the vehicle has started, and a stop() method that prints a simple message saying the vehicle has stopped.

# Next, create a child class called Car that inherits from Vehicle. A Car should have an additional attribute called number_of_doors. Add a simple drive() method that prints a message saying the car is driving. Override the display_info() method so that it also displays the number of doors. Inside the overridden method, use super() to call the parent's display_info() method.

# Then create another child class called Motorcycle that also inherits from Vehicle. A Motorcycle should have an additional attribute called engine_cc, representing the engine size. Add a simple ride() method that prints a message saying the motorcycle is being ridden. Override display_info() so that it also displays the engine size. Again, use super() to call the parent's display_info() method.

# Your class structure should look like this:

# Vehicle ├── Car └── Motorcycle

# The Vehicle class should have start(), stop(), and display_info() methods. The Car should have a drive() method, while the Motorcycle should have a ride() method. Both child classes should override display_info() and use super().

# Finally, create one Car and one Motorcycle and test their methods

class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("-----vehicle info-----")
        print(f"brand = {self.brand}")
        print(f"model = {self.model}")
        print(f"year = {self.year}")

    def start(self):
        print(f"{self.brand} {self.brand} has started")

    def stop(self):
        print(f"{self.brand} {self.brand} has stopped")

class Car(Vehicle):
    def __init__(self,brand,model,year,number_of_doors):
            super().__init__(brand,model,year)
            self.number_of_doors = number_of_doors

    def drive(self):
        print(f"{self.brand} {self.model} is driving")

    def display_info(self):
        super().display_info()
        print(f"Number of doors = {self.number_of_doors}")

class Motorcycle(Vehicle):
    def __init__(self,brand,model,year,engine_cc):
            super().__init__(brand,model,year)
            self.engine_cc = engine_cc

    def ride(self):
        print(f"{self.brand} {self.model} is being ridden")

    def display_info(self):
        super().display_info()
        print(f"Engine size is = {self.engine_cc}cc")

car1 = Car("BMW","M4",2020,4)
print("-------CAR-------")
car1.display_info()
car1.start()
car1.drive()
car1.stop()

motorcycle1 = Motorcycle("Kawasaki","MT-07",2023,689)
print("------MOTORCYCLE------")
motorcycle1.display_info()
motorcycle1.start()
motorcycle1.ride()
motorcycle1.stop()



