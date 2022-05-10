import turtle
from math import (
    sqrt,
)  # allows you to not have to write math before function | math.sqrt() -> sqrt()

# x1, y1 = eval(input("Enter x1, y1: "))
# x2, y2 = eval(input("Enter x2, y2: "))
# distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# x3 = (x2 + x1) / 2
# y3 = (y2 + y1) / 2

# turtle.showturtle()
# turtle.penup()
# turtle.goto(x1, y1)
# turtle.pendown()
# turtle.goto(x2, y2)
# turtle.penup()
# turtle.goto(x3, y3)
# turtle.write(distance)
# turtle.done()


# print("Hello", "Python", sep="***", end="++")
# By default sep = "_" and end = "\n"


amount = 187
dollars = amount // 100
remainder = amount % 100

quarter = remainder // 25
remainder = remainder % 25

dime = remainder // 10
remainder = remainder % 10

nickle = remainder // 5
remainder = remainder % 5

print(dollars, end=": dollar ")
print(quarter, end=": quarter ")
print(dime, end=": dime ")
print(nickle, end=": nickle ")
print(remainder, end=": penny ")

# In python all variables hold references of objects
# All objects have unique IDs
# id(x) - used to find the unique ID of an object
# Immutable - unchangeable "Objects are Immutable" "

# " Objects with the same value have the same unique ID"
