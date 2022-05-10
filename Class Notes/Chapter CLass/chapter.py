class TV:
    def __init__(self):
        self.volume = 0
        self.channel = 0
        self.on = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def volumeUp(self):
        self.volume += 1

# Data Field Encapsulation
# Always stop the user from directly accedssuing the property
# Private Properties are defined by double underscore, and you have to use underscore when referring to the property
# When properties are private you can't access them directly


class Circle:
    def __init__(self, radius=10):
        self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * 3.14

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius


# Class Abstraction and Encapsulation
# class abstraction means to seperate class implementation from the use of the class.
# Abstraction. User cares about usage. Make the system an Abstract System


weight = eval(input("Weight: "))
height = eval(input("Weight: "))
name = input("Name: ")
print(name, getBMI(weight, height))


def getBMI(weight, height):
    return weight // height ** 2

# If you refractor the function (methods) and the variables (properties) you create a class


# UML Diagram
# in UML Diagrams a "-" before a variable means it is private


# Compiler vs Interpreter
# Interpreters read line by line
# Compilers read the whole file


# Procedural Programming is subset of Object Oriented
# Procedural is functions, Object Oriented is classes
