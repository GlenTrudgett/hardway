# Study drills - 1 

cars = 100
# Changing the space_in_a_car to an integer, instead of floating point.
#space_in_a_car = 4.0
space_in_a_car = 4

# This makes no difference to the calculation, but in reality
#you not going to put in "half" a person!

drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "in each car.")


