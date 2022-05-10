# Associativity Rule - for () precedence L -> R,  * / // %  L -> R,   + - L -> R,   = R -> L
# +=, -=, *=, /=, %=

# Java - "final" means the variable can't be changed
# normally variables prefaced with final are written in uppercase
# Adopt Java convetion in python by making variable all uppercase to let others know not to change things
# // - looks for the quotient
# % - looks for the remainder

# Days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
# today = eval(input("Enter 0 Sat, 1 for Sun"))
# print("today is: " + Days[today])
# numOfDays = eval(input("Enter the number of days passed: "))
# dateCal = (today + numOfDays) % 7
# print(numOfDays + "days aways is" + Days[dateCal])


# 3700 seconds


# numOfSeconds = eval(input("Enter Seconds: "))


def secondsTimer(seconds):
    hours = seconds // (60 * 60)
    remainderOne = seconds % (60 * 60)
    minutes = remainderOne // 60
    remainderTwo = remainderOne % 60
    print(
        "Hours: "
        + str(hours)
        + " "
        + "Min: "
        + str(minutes)
        + " "
        + "Seconds: "
        + str(remainderTwo)
    )


# secondsTimer(numOfSeconds)

# Overflow: when a variable is assigned a value that is too large in size to be stored
# Underflow: when a floating-point
# Scientific Notation: 2e3 -> 2000 -> 2 x 10^3


# tax = 6.7487837621
# output = 6.74

# time = int(tax * 100) / 100
# print(time)

# test = round(tax, -1)
# print(test)


# Question 8
radius = 5.5
pie = 3.14

area = radius * radius * pie
perimeter = 2 * radius * pie

print(area)
print(perimeter)

# Question 9
width = 4.5
height = 4.5

area = width * height
perimeter = 2 * (width + height)

print(area)
print(perimeter)

# Question 11
yearInSeconds = 365 * 86400
birthPerYear = yearInSeconds / 7
deathPerYear = yearInSeconds / 13
immigrantPerYear = yearInSeconds / 45

displacement = birthPerYear - deathPerYear + immigrantPerYear

for i in range(1, 6, 1):
    currentPopulation = 312032486
    newPopulation = (i * displacement) + currentPopulation
    print(newPopulation)


# Question 12
