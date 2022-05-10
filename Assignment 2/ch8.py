# Chapter08: 1,4,7,11,12,13
from math import sqrt

#8 - 1


def sumColumn():
    sumList = []
    mastList = []
    rowLen = 0
    for i in range(3):
        # f formats the text to accept employeeProfilesariable i
        row = input(f"Enter 3-by-4 matrix row {i}: ").split(" ")
        rowLen = len(row)
        mastList.append(row)

    for s in range(rowLen):
        sum = 0
        for l in range(3):
            sum = sum + float(mastList[l][s])
        sumList.append(sum)

    for x in range(len(sumList)):
        print(f"The sum of the elements in column {x} is", sumList[x])
    return


sumColumn()


#8 - 4
employeeProfiles = [["Employee 0", 2, 4, 3, 4, 5, 8, 8],
                    ["Employee 1", 7, 3, 4, 3, 3, 4, 4],
                    ["Employee 2", 3, 3, 4, 3, 3, 2, 2],
                    ["Employee 3", 9, 3, 4, 7, 3, 4, 1],
                    ["Employee 4", 3, 5, 4, 3, 6, 3, 8],
                    ["Employee 5", 3, 4, 4, 6, 3, 4, 4],
                    ["Employee 6", 3, 7, 4, 8, 3, 8, 4],
                    ["Employee 7", 6, 3, 5, 9, 2, 7, 9]]


class Employee:
    def __init__(self, employeeName, mon, tue, wed, thur, fri, sat, sun):
        self.__employeeName = employeeName
        self.__mon = mon
        self.__tue = tue
        self.__wed = wed
        self.__thur = thur
        self.__fri = fri
        self.__sat = sat
        self.__sun = sun

    def getHoursList(self):
        hourList = [self.__mon, self.__tue, self.__wed,
                    self.__thur, self.__fri, self.__sat, self.__sun]
        return hourList

    def getSum(self):
        newList = self.getHoursList()
        sum = 0
        for i in range(len(newList)):
            sum = sum + newList[i]
        return sum

    def getEmployeeName(self):
        return self.__employeeName


def hourConvert(employeeProfiles):
    employeeProfTable = []
    sortedList = []
    for i in range(len(employeeProfiles)):
        employ = Employee(employeeProfiles[i][0], employeeProfiles[i][1], employeeProfiles[i][2], employeeProfiles[i]
                          [3], employeeProfiles[i][4], employeeProfiles[i][5], employeeProfiles[i][6], employeeProfiles[i][7])
        employeeProfTable.append(employ)

    temp = employeeProfTable[0].getSum()
    for l in range(len(employeeProfTable)):
        temp = employeeProfTable[l].getSum()
        if employeeProfTable[l].getSum() > temp:
            sortedList.append(employeeProfTable[l])
        else:
            for p in range(len(employeeProfTable)):
                if employeeProfTable[p].getSum() == temp:
                    sortedList.insert(p - 2, employeeProfTable[p])

    for m in range(len(sortedList)):
        z = m * -1
        name = sortedList[m].getEmployeeName()
        sums = sortedList[m].getSum()
        print("name: " + name + " sum: " + str(sums))
    return


print(hourConvert(employeeProfiles))
# 8 - 11


def diceGame():
    dice = ['T', 'H']
    userInput = input("Enter a number between 0 and 512: ")
    mat = matrixConemployeeProfilesert(userInput)

    for o in range(len(mat)):
        for j in range(3):
            listemployeeProfilesal = int(mat[o][j])
            print(dice[listemployeeProfilesal], end=" ")
        print("\n")
    return


def getBinary(num):
    binary = 0
    inc = 0
    adj = int(num)

    # conemployeeProfileserts the number to binary
    while(adj > 0):
        binary = ((adj % 2) * pow(10, inc)) + binary
        adj = int(adj / 2)
        inc += 1

    # adds extra zeros to binary number
    strBinary = str(binary)
    newState = ""
    for x in range(len(strBinary), 9):
        extraZero = "0"
        newState = newState + extraZero

    # returns a string
    return newState + strBinary


def matrixConemployeeProfilesert(stringemployeeProfilesal):
    wholeList = "".join(getBinary(stringemployeeProfilesal))
    sec1 = wholeList[0:3]
    sec2 = wholeList[3:6]
    sec3 = wholeList[6:9]

    realMatrix = []
    realMatrix.append(sec1)
    realMatrix.append(sec2)
    realMatrix.append(sec3)

    return realMatrix


diceGame()


# 8 - 12
# comeback too
rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]
brackets = [[8350, 33950, 82250, 171550, 372950], [16700, 67900, 137050, 208850, 372950], [
    8350, 33950, 68525, 104425, 186475], [11950, 45500, 117450, 190200, 372950]]

taxs = brackets[0][0] * rates[0] + (brackets[0][1] - brackets[0][0]) * rates[1]
tax = brackets[0][0] * rates[0] + (brackets[0][1] - brackets[0][0]) * rates[1] + (brackets[0][2] - brackets[0][1]) * rates[2] + (
    brackets[0][3] - brackets[0][2]) * rates[3] + (brackets[0][4] - brackets[0][0]) * rates[3] + (400000 - brackets[0][4]) * rates[5]
print(taxs)


#8 - 13
def locateLargest():
    numRows = int(input("Enter the number of rows in the list: "))
    masterList = []
    rowCounter = []
    for i in range(numRows):
        rows = input("Enter a row: ").split(" ")
        count = len(rows)
        rowCounter.append(count)
        masterList.append(rows)

    largestEl = 0
    specRow = 0
    specCol = 0
    for x in range(len(masterList)):
        for y in range(rowCounter[x]):
            masteremployeeProfilesal = float(int(masterList[x][y]))
            if masteremployeeProfilesal > largestEl:
                largestEl = masteremployeeProfilesal
                specRow = x
                specCol = y

    location = []
    location.append(specRow)
    location.append(specCol)
    return location
    # return employeeProfilesalue is a one-dimensional list
    # that contains two elements indicating row and column indexes


print("the location of the largest element is at ", locateLargest())
