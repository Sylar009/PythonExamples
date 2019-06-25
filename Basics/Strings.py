name = "My name is Sylar009"
date = "26 June 2019"

print(date)

longString = "This is long String and can be of any length."
print(longString)

shortString = "a"
print(shortString)

# Concating name and date with "+" Operator
newString = name + ", " + date
print(newString)

# Multipling the string with "*" Operator
multiply = shortString * 5
print(multiply)

multiply2 = date * 2
print(multiply2)

# Every charter of a string is at particular index
# So we will work on indexing.
print(date[3])
print(date[4])

# We can also specify the range of indexes
# Printing the month by applying range.
print(date[3:7])

# Let's try this on name string
print(name[0:2])

# By not specifying the upper limit it will print the complete string
print(name[3:])

# we can use negative index i.e. last digit is -1 of the string
# If we want to print the month using negative index
print(date[-9:-5])
