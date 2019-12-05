# class Dog():
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         print(self.name.title() + "roll_overed")

# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
#
# print(my_dog.name.title())
# print(my_dog.name + "'s age is " + str(my_dog.age))
#
# my_dog.sit()

class Car():
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + "  " + self.make + "  " + self.model
        return long_name.title()

    def read_oldmeter(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car(2016, "audi", "a4")
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(16)
my_new_car.read_oldmeter()