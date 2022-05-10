import turtle
tut = turtle.Turtle()

# method to draw square


def sq():
    for i in range(4):
        tut.forward(30)
        tut.left(90)
    tut.forward(30)


# loops for board
for i in range(8):
    # not ready to draw
    tut.up()
    # set position for every row
    tut.setpos(0, 30 * i)
    # ready to draw
    tut.down()
    # row
    for j in range(8):
        # conditions for alternative color
        if (i + j) % 2 == 0:
            col = 'black'
        else:
            col = 'white'
        # fill with given color
        tut.fillcolor(col)
        # start filling with colour
        tut.begin_fill()
        # call method
        sq()
        # stop filling
        tut.end_fill()
# hide the turtle
    tut.hideturtle()
