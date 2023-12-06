# car.py
from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

# Create an instance of Car
my_car = Car(wheel_size=18, wheel_number=4)

# Access methods and attributes on the instance
print(my_car.go())              # Output: VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!
print(my_car.fill_up_tank())    # Output: filling up!
print(my_car.wheel_size)        # Output: 18
print(my_car.wheel_number)      # Output: 4
