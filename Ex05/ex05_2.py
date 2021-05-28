# Study Drill #1 - remove "my_"

name = 'Zed A. Shaw'
age  = 35 # not a lie
height   = 74 # inches
weight   = 180 # lbs
eyes     = 'Blue'
teeth    = 'White'
hair     = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not to heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# and now in Metric!!

m_weight = weight * 0.4535
m_height = height * 2.5

print(f"{name} has his metric measurements too!")
print(f"He weighs {m_weight} kg's and is {m_height} cm's tall!")



