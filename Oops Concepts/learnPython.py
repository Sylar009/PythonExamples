# making first class
class Person:
    # variables in class
    name = ""
    age = ""
    gender = ""
    height = 0

    # Making Constructor of the class
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    # Methods in class
    def eat(self):
        print("Eating ...")

    def walk(self):
        print("Walking ...")

    def getName(self):
        print("returning name = " + self.name)
        return self.name

    def getAge(self):
        print("returning age = " + self.age)
        return self.age


# creating an object of Person class
person = Person("Sylar009", 25, "Male", 6)

# calling methods of Person Class
person.eat()
person.walk()
print(person.getName())

# Creating another person
person2 = Person("SamWise", 30, "Male", 5.5)
print(person2.getName())