#This is interesting.. the formatter is just a variable.
#Nothing fancy to be seen, but you can change the position
#of the text with space. 

#formatter = "{} {}    {} {}"
formatter = "{} {} {} {}"
sexy = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

print(sexy.format(1, 2, 3, 4))
print(sexy.format("one", "two", "three", "four"))
print(sexy.format(True, False, False, True))
print(sexy.format(formatter, formatter, formatter, formatter))

print(formatter. format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

