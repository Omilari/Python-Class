# Chapter06: 1,4,5,10,12,18,47,48
import random
import turtle
tut = turtle.Turtle()

# 6 - 1 : Done


def getPentagonalNumber(n):
    penNum = (n * (3 * n - 1)) / 2
    return (penNum)


def PenNumHundred():
    x = 1
    while x <= 100:
        print(int(getPentagonalNumber(x)), end="  ")
        if(x % 10 == 0):
            print('\n')
        x += 1


# 6 - 4 : Done but could improve
def reverse(num):
    rev = 0
    while num > 0:
        remainder = num % 10
        rev = rev * 10 + remainder
        num //= 10
    return rev


print(reverse(18923))


#6 - 5
def displaySortedNumbers(num1, num2, num3):
    if num1 < num2:
        if num1 > num3:
            return num3, num1, num2
        elif num3 < num2:
            return num1, num3, num2
    else:
        if num1 < num3:
            return num2, num1, num3
        else:
            return num2, num3, num1


# num1 < num2 < num3
print(displaySortedNumbers(1, 2, 3))


# 6 - 10 : Done
def isPrime(n):
    half_n = int(n / 2)
    if (n < 2):
        return False
    for i in range(2, half_n):
        if (n % i == 0):
            return False
    return True


def listIsPrime(target):
    x = 0
    while x < target:
        if isPrime(x):
            print(x, " is a prime number")
        x += 1


# 6 - 12: Done
def printchars(ch1, ch2, numberPerLine):
    if ord(ch2) < ord(ch1):
        largestch = ord(ch1)
        smallerch = ord(ch2)
    else:
        largestch = ord(ch2)
        smallerch = ord(ch1)

    inc = 0
    for i in range(smallerch, largestch):
        char = ord(ch1)
        print(chr(i), end=" ")
        inc += 1
        if inc % numberPerLine == 0:
            print('\n')


#printchars("1", "Z", 10)


# 6 - 18 : Done
def printMatrix(n):
    for i in range(n):
        for x in range(n):
            print(random.randint(0, 1), end=" ")
        print('\n')


# printMatrix(4)


#6 - 47
def drawChessboard(startx, endx, starty, endy):
    print(startx)

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


# 6 - 48 : Done
def format(number, width):
    counter = 0
    newNum = number

    while newNum > 0:
        remainder = newNum % 10
        newNum = newNum // 10
        counter += 1

    for i in range(width - counter):
        print(0, end="")

    print(number)


format(213, 4)  # remainder - 3, number - 21,
