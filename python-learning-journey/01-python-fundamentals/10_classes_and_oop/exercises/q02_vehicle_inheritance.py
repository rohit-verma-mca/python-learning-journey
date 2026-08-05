"""
Question:
Create a base class Vehicle with attributes like make, model, and a
method describe(). Then create a Car subclass that inherits from
Vehicle and adds an extra attribute (like num_doors), overriding
describe() to include it.

"""


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def describe(self):
        base_description = super().describe()
        return f"{base_description} with {self.num_doors} doors"


if __name__ == "__main__":
    generic_vehicle = Vehicle("Yamaha", "FZ")
    print(generic_vehicle.describe())      # Yamaha FZ

    my_car = Car("Maruti Suzuki", "Swift", 4)
    print(my_car.describe())               # Maruti Suzuki Swift with 4 doors