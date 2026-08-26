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



