# Study drills - 3 

# The total number of cars
cars = 100
# Total amount of seating per car.
space_in_a_car = 4.0

# This represents the number of available drivers
drivers = 30
# The number of passengers available to be transported
passengers = 90

# If there is a driver per car, then we can calculate the cars not used
cars_not_driven = cars - drivers

# The number of cars that will be used in the pool available
cars_driven = drivers
# The number of people that can be transported 
carpool_capacity = cars_driven * space_in_a_car
# The average amount of passengers we can equally move, per car.
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "in each car.")


