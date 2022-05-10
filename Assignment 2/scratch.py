#8 - 7
from math import sqrt
points = [[-1, 0, 3], [-1, -1, -1], [4, 1, 1], [2, 0.5, 9],
          [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2], [5.5, 4, -0.5]]


def getDist(x, y, z, x2, y2, z2):
    diffSquared = pow((x2 - x), 2) + pow((y2 - y), 2) + pow((z2 - z), 2)
    sqDiff = sqrt(diffSquared)
    # print(sqDiff)
    return sqDiff


def findNearestPoints(pointList):
    # gets the starting distance
    listPos1 = 0
    listPos2 = 0
    startDist = getDist(pointList[0][0], pointList[0][1], pointList[0]
                        [2], pointList[1][0], pointList[1][1], pointList[1][2])
    print("start dist is: ", startDist)

    # creates a loop that
    for i in range(len(pointList)):
        x = i + 1
        for j in range(x, len(pointList) - x):
            z = j + 1
            # gets the distance of point i from all values aftwards
            pointDist = getDist(pointList[j][0], pointList[j][1], pointList[j][2],
                                pointList[z][0], pointList[z][1], pointList[z][2])
            # compares "startDist" with each "pointDist"
            # if "startDist" is larger, set it equal to "pointDist"
            # gets associated list positions for the points
            if startDist > pointDist:
                startDist = pointDist
                listPos1 = j
                #print("listPos1: ", listPos1)
                listPos2 = z
                #print("listPos2: ", listPos2)

    nearestPoints = "The points nearest to each other are " + \
        str(pointList[listPos1]) + " & " + \
        str(pointList[listPos2]) + " which is " + \
        str(startDist) + " units^3 away"
    return nearestPoints


print(findNearestPoints(points))
