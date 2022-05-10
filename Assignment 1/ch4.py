# Chapter04: 4,5,6,8,17
import math
import turtle

turtles = turtle.Turtle()
pi = math.pi
# Question 4
print("Find Area of Hexagon")
hex_side = float(input('Enter the length of the side: '))
hex_area = (6 * pow(hex_side, 2)) / \
    (4 * math.tan(pi / 6))
print('The area the hexagon is' + str(hex_area))


# Question 5
print("Find Area of Any Reg Polygon")
num_of_sides = int(input('Enter the number of sides: '))
poly_side = float(input('Enter the length of the side: '))
reg_area = (num_of_sides * pow(poly_side, 2)) / \
    (4 * math.tan(pi / num_of_sides))

print('The area a ' + str(num_of_sides) + ' sided polygon is ' + str(reg_area))

# 45 radius, top 110 x distance, bottom 55 x distance, 50 y difference = .41, .82, .9 110 x .41 = 45

# Question 6
star_len = float(input('enter the length: '))
for i in range(5):
    turtles.forward(star_len)
    turtles.right(144)

# Question 8
turt_radius = float(input("Enter a radius: "))
turtles.showturtle()
turtles.color("blue")
turtles.penup()
turtles.goto(-(turt_radius / .41), -(turt_radius / 1.8))
turtles.pendown()
turtles.circle(turt_radius)

turtles.color("black")
turtles.penup()
turtles.goto(0, -(turt_radius / 1.8))
turtles.pendown()
turtles.circle(turt_radius)

turtles.color("red")
turtles.penup()
turtles.goto((turt_radius / .41), -(turt_radius / 1.8))
turtles.pendown()
turtles.circle(turt_radius)

turtles.color("yellow")
turtles.penup()
turtles.goto(-(turt_radius / .82), -(turt_radius / .6))
turtles.pendown()
turtles.circle(turt_radius)

turtles.color("green")
turtles.penup()
turtles.goto((turt_radius / .82), -(turt_radius / .6))
turtles.pendown()
turtles.circle(turt_radius)


# Question 17
circ_radius = float(input('Enter the radius of the bounding circle: '))
turtles.circle(circ_radius)
# confused about why this doesn't work
# can change 5 to number of sides for polygon
theta = 1
while theta <= 5:
    x = circ_radius * math.cos((theta * (360 / 5)))
    y = circ_radius * math.cos((theta * (360 / 5)))
    turtles.goto(x, y)
