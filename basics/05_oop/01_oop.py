class car:
    def __init__(self, brand, model): # init is constructor
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = car("toyota", "corolla")

print(my_car.full_name())
print(my_car.model)

my_new_car = car("tata", "safari")

print(my_new_car.model)