# Chapter07: 1,2,3,4

# 7 - 1 : Done
def highScore():
    highestScore = 0
    letter_grade = ['A', 'B', 'C', 'D']
    listGrades = input(
        "Enter scores seperated by space from one line: ").split(" ")

    for i in range(len(listGrades)):
        if highestScore < float(listGrades[i]):
            highestScore = float(listGrades[i])

    for x in range(len(listGrades)):
        if float(listGrades[x]) >= highestScore - 10:
            print(listGrades[x], "scored an", letter_grade[0])
        elif float(listGrades[x]) >= highestScore - 20:
            print(listGrades[x], "scored an", letter_grade[1])
        elif float(listGrades[x]) >= highestScore - 30:
            print(listGrades[x], "scored an", letter_grade[2])
        elif float(listGrades[x]) >= highestScore - 40:
            print(listGrades[x], "scored an", letter_grade[3])
        else:
            print(listGrades[x], "scored an F")


highScore()
# get list of scores
# find highest score
# index finds location
# if highestscore - letter_grade


# 7 - 2 : Done
def reverseNum():
    num = int(input('Enter in the number of values in the list'))
    num_list = []
    for i in range(int(num)):
        n = input("Enter a value ")
        num_list.append(int(n))

    print('Original Array: ')
    for x in range(len(num_list)):
        print(num_list[x], end=" ")
    print('\n')
    print('Reverse Array: ')

    for x in range(1, len(num_list)):
        loc = -1 * x
        print(num_list[loc], end=" ")
    print(num_list[0])


reverseNum()


# 7 - 3
def counterFunc():
    userinput = input("Enter the integers between 1 and 100: ")
    inputList = userinput.split(" ")
    cleanList = []
    for x in inputList:
        if x not in cleanList:
            cleanList.append(x)

    for i in range(len(cleanList)):
        if userinput.split().count(f'{cleanList[i]}') > 1:
            print(cleanList[i], ' occurs ',
                  userinput.split().count(f'{cleanList[i]}'), ' times')
        else:
            print(cleanList[i], ' occurs ',
                  userinput.split().count(f'{cleanList[i]}'), ' time')


counterFunc()


#7 - 4
def aboveAverage():
    inputs = input('Enter list of scores: ').split(" ")
    total = 0.0
    aboveCount = 0
    belowCount = 0
    for i in range(len(inputs)):
        total = total + float(inputs[i])
    ave = total / len(inputs)
    print('Average is', ave)
    for x in range(len(inputs)):
        if ave >= float(inputs[x]):
            aboveCount += 1
        else:
            belowCount += 1

    print('Number of scores above or equal to the average:', aboveCount)
    print('Number of scores below the average:', belowCount)


aboveAverage()
