from tkinter import *
from turtle import RawTurtle, TurtleScreen


def countVowels():
    chars = tuple('abcdefghijklmnopqrstuvwxyz')
    file_name = input("Enter file name: ")
    new_file = open(file_name, 'r')
    contents = new_file.read()
    if contents == None:
        print("File Doesn't Exist")

    x = {c: contents.count(c) for c in chars}

    print("chars count:", x)

    # Creates windows
    window = Tk()
    window.title("Bar Chart")
    win_wid = 500
    win_canvas = Canvas(window, width=win_wid, height=win_wid)
    win_canvas.pack()
    t_screen = TurtleScreen(win_canvas)
    turt = RawTurtle(t_screen)
    turt.penup()
    turt.goto(-200, 0)
    turt.pd()
    for keyss in contents:
        fdist = (win_wid - 100) / 23
        turt.fd(fdist)
        turt.left(90)
        turt.fd(contents[keyss])
        turt.left(90)
        turt.fd(fdist)
        turt.left(90)
        turt.fd(contents[keyss])
        turt.left(90)
        turt.fd(contents[keyss])

    window.mainloop()


countVowels()


def createBar(turts, win_w):
    fdistance = (win_w - 100) / 23
    turts.fd(fdistance)
