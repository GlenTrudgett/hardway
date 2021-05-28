# This is a variable that is assigned the value of 10
types_of_people = 10

# This is a compound string, with a call to a variable and
# an f-string assigned to the variable 'x'
x = f"There are {types_of_people} types of people."

# Assign the String to the variable binary
binary = "binary"
# Assign another string to another variable.
do_not = "don't"

# This is a compound string, with a call to a variable and
# an f-string assigned to the variable 'y'
y = f"Those who know {binary} and those who {do_not}"

# Print the details and call of variable values to the console.
print(x)
print(y)

# a Good example of using an f-string in a print statement
print(f"I said: {x}")
# Use of single quotes in an f-string
print(f"I also said: '{y}'")

# Assigning the Boolean value 'False' to a variable
hilarious = False

#This is a string that uses the .format() command to pass variables into
joke_evaluation = "Isn't that joke so funny?! {}"

# print the variable joke evaluation and assign the variable hilarious to it.
print(joke_evaluation.format(hilarious))

#These are just strings assigned to the variables 'w' and 'e'
w = "This is the left side of..."
e = "a string with a right side."

# You can join strings together by using the + operator!
print(w + e)
