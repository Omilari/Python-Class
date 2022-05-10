# Chapter11: 2, 5, 13, 25

#11 - 2
def sumMajorDiagonal():
    mainList = []
    for x in range(4):
        userIn = input(f"Enter a 4-by-4 matrix row for row {x}: ").split(" ")
        temp = [float(p) for p in userIn]
        mainList.append(temp)
    sum = 0
    # sum of [0][0], [1][1], [2][2], [3][3]
    for i in range(len(mainList)):
        sum = sum + mainList[i][i]
    print("Sum of the elements in the major diagonal is", sum)
    return


sumMajorDiagonal()


#11 - 5
matrixA = input("Enter Matrix 1:").split(" ")
matrixB = input("Enter Matrix 2:").split(" ")


def addMatrix(a, b):
    matA = [float(x) for x in a]
    matB = [float(x) for x in b]
    matC = []
    for x in range(len(matA)):
        sum = matA[x] + matB[x]
        matC.append(sum)

    counter = 0
    for y in range(len(matC)):
        print(matC[y], end=" ")
        print("y:", y, end=" ")

        if (y / 3 == int(y / 3)):
            print()
    return


addMatrix(matrixA, matrixB)


#11 - 13
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
            masteremployeeProfilesal = float(masterList[x][y])
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


#11 - 25
def markovMat():
    # gets user input
    print("Enter a 3-by-3 row by row:")
    mastMat = []

    # adds inputs to Master Matrix
    for x in range(3):
        useIn = input("").split(" ")
        intList = [float(l) for l in useIn]
        mastMat.append(intList)

    isSumOne = True
    isPositive = True

    for p in range(len(mastMat)):
        sum = 0
        for v in range(len(mastMat[p])):
            # checks whether there is any negative values
            if mastMat[p][v] < 0:
                isPositive = False

            # sums the columns
            sum = sum + mastMat[v][p]

        # checks if the columns add to 1
        if sum != 1:
            isSumOne = False

    # both true: yes, else no
    if isSumOne & isPositive == True:
        print("The Matrix is a Markov Matrix")
    else:
        print("The Matrix is not a Markov Matrix")

    return


markovMat()
