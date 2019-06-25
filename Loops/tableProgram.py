
#Enter a number by user input and writing table of it using for loop
number = int(input("Please enter a number"))
for value in range(1, 11):
    print(str(number) + " x " + str(value) + " = " + str(number*value))