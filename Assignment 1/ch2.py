# Assignment#1:
# Chapter02: 3,5,12,14,19,26

# Question 3
from cmath import sqrt
import turtle
turt = turtle.Turtle()

feet = float(input('enter in the number of feet: '))
print('Is Meter: ' + str(eval('feet * .305')))

# Question 5
subtotal = float(input('Enter your Subtotal here: '))
gratuity_rate = int(input('Enter your Gratuity Rate here: '))

gratuity_value = (gratuity_rate / 100) * subtotal
total = subtotal + gratuity_value
print('The gratuity is ' + str(round(gratuity_value, 2)) +
      ' and total is ' + str(round(total, 2)))


# Question 12
count = int(input('enter the number to count too:'))
a = 1
print("a    b   pow(a,b)")
while a < count + 1:
    b = a + 1
    print(str(a) + "    " + str(b) + "   " + str(pow(a, b)))
    a += 1

# Question 14
x1, y1 = eval(input('enter your x1 and y1 values: '))
x2, y2 = eval(input('enter your x2 and y2 values: '))
x3, y3 = eval(input('enter your x3 and y3 values: '))

Side1 = sqrt(pow((y2 - y1), 2) + pow((x2 - x1), 2))
Side2 = sqrt(pow((y3 - y2), 2) + pow((x3 - x2), 2))
Side3 = sqrt(pow((y1 - y3), 2) + pow((x1 - x3), 2))


s = (Side1 + Side2 + Side3) / 2
area = sqrt(s * (s - Side1) * (s - Side2) * (s - Side3))
print('The area of the triangle is ' + str(area))

# Question 19
investment_amount = float(input('Enter Investment Amount: '))
annual_int_rate = float(input('Enter Investment Amount: '))
num_years = float(input('Enter Investment Amount: '))

mon_interest_rate = (annual_int_rate / 100) / 12
num_mon = num_years * 12

future_invest_value = round(
    investment_amount * pow((1 + mon_interest_rate), num_mon), 2)

print("Future Investment Amount: " + str(future_invest_value))


# Question 26
# Turtle: draw four circles; write a program that prompts
# the user to enter the radius and draws four circles on the screen,
# as shown in Figure 2.4
turt_rad = float(input('Enter the circle radius: '))
turt.showturtle()
turt.penup()
turt.goto(0, 0)
turt.pendown()
turt.circle(turt_rad)
turt.penup()
turt.goto(2 * turt_rad, 0)
turt.pendown()
turt.circle(turt_rad)
turt.penup()
turt.goto(0, -(2 * turt_rad))
turt.pendown()
turt.circle(turt_rad)
turt.penup()
turt.goto((2 * turt_rad), -(2 * turt_rad))
turt.pendown()
turt.circle(turt_rad)
