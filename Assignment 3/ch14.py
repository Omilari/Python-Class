# Chapter14: 2, 3, 5, 10, 11
from turtle import RawTurtle, TurtleScreen
from tkinter import *
import random

#14 - 2


def mostOccur():
    # gets values
    l2 = input("Enter in List of numbers: ").split(" ")
    # turns values to ints
    for i in range(len(l2)):
        l2[i] = int(l2[i])
    # sorts values
    l2.sort()
    print(l2)
    # create dictionary with keys from list values
    dic = {}
    for i in range(len(l2)):
        if l2[i] not in dic:
            dic[l2[i]] = l2.count(l2[i])

    # prints the keys and values of the dictionary
    maxVal = 0
    for keyss in dic:
        if(dic[keyss] > maxVal):
            maxVal = dic[keyss]

    mostOften = []
    for keyys in dic:
        if(dic[keyys] == maxVal):
            mostOften.append(keyys)

    print(mostOften, "appears the most often")


mostOccur()


# 14-3
def somethingDiff():
    file_name = input("Enter a file name: ")
    newFile = open(file_name, 'r')
    charTup = tuple('!@#$%^&*()<>?,./`~|-')
    otherTup = tuple('\n')
    contents = newFile.read()
    contents = contents.lower()

    for chars in contents:
        if chars in charTup:
            contents = contents.replace(chars, '')
        if chars in otherTup:
            contents = contents.replace(chars, ' ')

    contentList = contents.split(" ")
    contentSet = set(contentList)
    dic = {}
    for b in contentSet:
        dic[b] = contents.count(b)

    for keyss in dic:
        print(keyss, "  appears", dic[keyss], "times")


#14 - 5


def char_bargraph():
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


char_bargraph()


def createBar(turts, win_w):
    fdistance = (win_w - 100) / 23
    turts.fd(fdistance)


#14 - 10
def state_cap_game():
    #state : capital
    state_to_cap = {'Alabama': 'Mongomery',
                    'Alaska': 'Juneau', 'Arizona': 'Pheonix'}

    # randomize
    state_lists = list(state_to_cap.items())
    random.shuffle(state_lists)
    new_dict = dict(state_lists)
    score = 0

    for states in new_dict:
        states_string = str(states)
        user_guess = input('What is the capital of ' + states_string + '? ')
        user_guess = user_guess.capitalize()
        if new_dict[states] == user_guess:
            print("Your answer is correct")
            score += 1
        else:
            print("The correct answer should be", new_dict[states])

    return score


print("The correct count is", state_cap_game())


#14 - 11
def countVowels():
    vowels = set('aeiou')
    consonants = tuple('bcdfghjklmnpqrstvwxyz')
    file_name = input("Enter file name: ")
    new_file = open(file_name, 'r')
    contents = new_file.read()
    dic = {}

    x = {v: contents.count(v) for v in vowels}
    y = {v: contents.count(v) for v in consonants}

    print("vowel count:", x)
    print("consonants count:", y)


countVowels()
