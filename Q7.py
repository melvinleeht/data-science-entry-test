class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def __init__(self, make, model, year):
        if not isinstance(make, str) or not isinstance(model, str) or not isinstance(year, int):
            raise TypeError("Make and model must be strings, year must be an integer")
        self.make = make
        self.model = model
        self.year = year
        return None

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")



# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
car1 = Car("Toyota", "Corolla", 2020)
car1.describe_car()
