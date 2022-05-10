# Chapter10: 2, 3, 9, 10, 12, 13
#https://foobar.withgoogle.com/#
from math import sqrt

# ch 10 - 2
l1 = [3, 5, 6, 2, 5, 43, 65]

# v1
def revList(specList):
    specList.reverse()
    return specList

print(revList(l1))

# v2
def reverseList(sList):
    num = len(sList) * -1
    sList[-1:num]
    return sList

print(reverseList(l1))


# 10 - 3
def NumOccur():
    # gets values
    l2 = input("Enter in numbers from 1 to 100: ").split(" ")
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
    for keyss in dic:
        if(dic[keyss] > 1):
            print(keyss, "occured", dic[keyss], "times")
        else:
            print(keyss, "occured", dic[keyss], "time")


NumOccur()


# 10 - 9
def StanDev():
    # gets user input
    numList = input("Enter a list of numbers seperated by space: ").split(" ")

    # converts to floar
    for i in range(len(numList)):
        numList[i] = float(numList[i])

    # gets and prints the mean of converted list
    l1Mean = calcMean(numList)
    print("The mean value for the list:", l1Mean)

    # logic for stan dev
    diffSquared = [pow((x - l1Mean), 2) for x in numList]
    DiffSqSum = calcMean(diffSquared) * len(diffSquared)

    # returns Stan Dev
    return sqrt(DiffSqSum / (len(numList) - 1))


def calcMean(l1):
    sum = 0
    for i in range(len(l1)):
        sum += l1[i]
    return sum / len(l1)


print("The Standard Deviation for this list:", StanDev())


# 10 - 10
def ReversesList():
    userList = input("Enter a list of inputs sep by space:").split(" ")
    return [userList[i] for i in range(len(userList) - 1, -1, -1)]


print(ReversesList())


# 10 - 12
def GCD():
    userNum = input("Enter a list of 5 numbers:").split(" ")
    c = 0

    for i in range(len(userNum)):
        userNum[i] = float(userNum[i])

    print(userNum)
    checkTill = int(min(userNum) / 2)
    print(checkTill)
    for i in range(0, checkTill, 1):
        counter = 0
        for x in range(len(userNum)):
            if userNum[x] % (checkTill - i) == 0 & counter < len(userNum):
                counter += 1
                print("counter:", counter)
                print("values:", x, checkTill -
                      i, userNum[x] % (checkTill - i))
            elif counter == len(userNum):
                c = checkTill - i
                break
            else:
                continue

    return c


#print("GCD:", GCD())


#10 - 13
def elimDups():
    list1 = input("Enter in a list of numbers: ").split(" ")
    [int(x) for x in list1]
    s = set(list1)
    print("The Distinct Numbers:", end=" ")
    for elems in s:
        print(elems, end=" ")
    return


elimDups()
