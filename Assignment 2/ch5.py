# Chapter05: 2,10,12,14,20,55

from cmath import sqrt
import random


#5 - 2 10 random addition questions
class randNumber:
    def __init__(self, lowerBound, upperBound):
        # Assigns variables to randon numbers
        self.num1 = random.randint(lowerBound, upperBound)
        self.num2 = random.randint(lowerBound, upperBound)

    def randSubtract(self):
        # function subtracts the numbers
        return self.num1 - self.num2

    def randAddition(self):
        # function adds the numbers
        return self.num1 + self.num2

    def getNum1(self):
        # gets the value
        return self.num1

    def getNum2(self):
        # gets the value
        return self.num2


def randUserGuess(lowerbound, upperbound, len):
    # function that loops the calculations based on user inputs
    counter = 0
    for i in range(len):
        x = randNumber(lowerbound, upperbound)
        randSub = x.randSubtract()
        randAdd = x.randAddition()
        num1 = x.getNum1()
        num2 = x.getNum2()
        print("What is ", str(num1), " + ", str(num2), ": ", end="")
        userGuess = eval(input(""))
        if(userGuess == randAdd):
            print('you got it correct')
            continue
            counter += 1
        else:
            print('you got it wrong')

        if counter == 3:
            print('you have no more guess. Try again.')
            break


lbound = eval(input("Enter lowerbound: "))
ubound = eval(input("Enter lowerbound: "))
ran = eval(input("Enter the length: "))
randUserGuess(lbound, ubound, ran)


def compareInt(num1, num2):
    if num1 > num2:
        return(num1)
    else:
        return(num2)


print(compareInt(12, 34))


def increment(num):
    return num + 1

# 5 - 10
def highestScore():
    numScores = int(input('Enter the number of participants: '))
    highestVal = 0
    highestName = ''
    for i in range(numScores):
        studName = str(input('Enter Student Name: '))
        studScore = int(input('Enter the Associated Student Score: '))
        if(studScore > highestVal):
            highestVal = studScore
            highestName = studName
        i += 1

    print('Top student ' + highestName + "'s score is " + str(highestVal))


# 5 - 12 - number divisible by 5 or 6 but not both
def underStand():
    lowerBound = 100
    upperBound = 1000
    while lowerBound < upperBound:
        isAndDivisible = lowerBound % 5 == 0 & lowerBound % 6 == 0
        isOrDivisible = lowerBound % 5 == 0 or lowerBound % 6 == 0

        if(isOrDivisible):
            print(lowerBound, end=" ")
        lowerBound += 1


#5 - 14
def smalln2(userInput):
    target_num = userInput
    n = 1
    while n <= target_num / n:
        n += 1
    print(n - 1)


tar_num = float(input('Enter the target number: '))
smalln2(tar_num)


#5 - 20

# Pattern A
# n = 1
# while n <= 6:
#    m = 1
#    while m < n:
#        print(m, end=" ")
#        m += 1
#    print(end="\n")
#   n += 1

#n = 1
# while n <= 6:
#    m = 1
#    while m <= 7 - n:
#        print(m, end=" ")
#        m += 1
#    print(end="\n")
#    n += 1


# Pattern C
#n = 1
# while n <= 6:
#    m = 1
#    while m <= 6 - n:
#        print("  ", end="")
#       m += 1
#    o = 1
#    while o <= n:
#        print(o, end=" ")
#        o += 1
#    print(end="\n")
#    n += 1


#
