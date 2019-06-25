# making first class
class Person:

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


# Inheriting Person Class

class Student(Person):
    rollNumber = 0
    marks = 100

    def takeClass(self):
        print("Taking Class ...")


student = Student("Sylar009", 25, "Male", 6)

student.eat()
student.takeClass()
