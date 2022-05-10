from cmath import pi
import turtle
# Assignment#1:
# Programming Exercises of the Book:

# Chapter01: 8,9,11,12


#   problem 8
# write a program that display the area and perimeter
# of a circle that has a radius of 5.5 using the formula given
turt = turtle.Turtle()
# plug 5.5 in user input
radius = float(input('Enter an radius: '))

area = radius * radius * pi
perimeter = 2 * radius * pi

print("the area is:" + str(area))
print("the perimeter is:" + str(perimeter))

# problem 9
width = float(input('Enter a width: '))
height = float(input('Enter in a height: '))

area2 = width * height
perimeter2 = 2 * width + 2 * height

print("the area is:" + str(area2))
print("the perimeter is:" + str(perimeter2))


# Question 11
years = int(input('Enter in the number of years you want to predict: '))
yearInSeconds = 365 * 86400
birthPerYear = yearInSeconds / 7
deathPerYear = yearInSeconds / 13
immigrantPerYear = yearInSeconds / 45

displacement = birthPerYear - deathPerYear + immigrantPerYear

for i in range(1, years + 1, 1):
    currentPopulation = 312032486
    newPopulation = (i * displacement) + currentPopulation
    print(newPopulation)


# Question 12
turt_rad = float(input('Enter the length of a side: '))
turt.showturtle()

for i in range(4):
    for x in range(4):
        turt.forward(turt_rad)
        turt.right(90)
    turt.right(90)
