import collections
def funcDroo(xCoordinate, yCoordinate):

    xSeen = collections.defaultdict(int)
    ySeen = collections.defaultdict(int)
    maxx = 0
    for x, y in zip(xCoordinate, yCoordinate):
        xSeen[x] += 1
        ySeen[y] += 1
        maxx = max(maxx, xSeen[x], ySeen[y])

    return maxx


input = [2,3,2,4,2]
input2 = [2,2,6,5,8]
print(funcDroo(input, input2))


