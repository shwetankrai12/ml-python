class Car:

    total_car = 0

    def __init__(self, brand, model): # init is constructor
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport that run on roads and are powered by engines."
    @property
    def model(self):
        return self.__model

class EleectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


    def fuel_type(self):
        return "electric charge"

# my_tesla = EleectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla,EleectricCar))
# print(my_tesla.__brand)
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# my_car.model = "city"
# Car("Tata", "Nexon")


# print(Car.total_car)
# print(my_car.general_description())
# print(my_car.model)




# my_Car = Car("toyota", "corolla")

# print(my_Car.full_name())
# print(my_Car.model)

# my_new_Car = Car("tata", "safari")

# print(my_new_Car.model)



class Battery:
    def battery_info(self):
        return "This is battery."

class Engine:
    def engine_info(self):
        return "This is engine."


class EleectricCarTwo(Battery, Engine,Car):
    pass

my_new_tesla = EleectricCarTwo("Tesla", "Model S")


print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())