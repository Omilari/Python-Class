import turtle


turtle.showturtle()
startx = -150
starty = -150

for i in range(0, 16):
    turtle.penup()
    turtle.goto(startx, starty)
    turtle.pendown()
    turtle.forward(200)
    starty = starty + 10

turtle.done()
