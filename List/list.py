# Lets create our first List
firstList = [1, 2, 3]
print(firstList)

# Lets create a hetrogenous list
anotherList = [1, "abc", 30]
print(anotherList)

# lets create nested list
list2 = [1, "abc", [30, "Sylar009"],4, 88, "Python"]
print(list2[1])
print(list2[0:2])
print(list2[1:3])
print(list2[2:])
print(list2[:4])

str = list2[1]
print(str)

# Getting element of nested list
str1 = list2[2][1]
print(str1)

# Getting particular character from string in the list
str2 = list2[1][2]
print(str2)

# Using functions in list ######
fruits = ["apple", "orange"]
print(fruits)

# using "Append" fucntion
fruits.append("mango")
fruits.append(67)
print(fruits)

# using Extend Function
fruits.extend("banana")
print(fruits)

# using insert function "Insert"
fruits.insert(1, "Grapes")
print(fruits)