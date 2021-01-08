import tree

# Read in lines in order starting from 1 (root of slopes)

def reorder(slopes): # List of lists, where each list contains starting pt, ending pt, capacity, and cost
    slopeCount = 0
    newSlopes = []
    found = []
    seen = [1]
    while (slopeCount < len(slopes)):
        recentlySeen = []
        for slope in slopes:
            if ((slope[0] in seen) and not (slope[0] in found)):
                newSlopes.append(slope)
                recentlySeen.append(slope[1])
                slopeCount += 1
        found += seen
        seen = recentlySeen
    return newSlopes

def buildTree(slopes):
    newTree = tree.Tree()
    newTree.setRoot(1)
    for slope in len(slopes):
        newTree.insert(slope[0], slope[1], slope[2], slope[3])
    return newTree

def solve(tree):
    pass

if __name__ == "__main__":

    testCases = input()
    for caseNum in range(1, testCases + 1):
        slopes = []
        restPoints = input()
        for restPoint in range(1, restPoints):
            slope = []
            slope.append(input()) # Slope starting rest point
            slope.append(input()) # Slope ending rest point
            slope.append(input()) # Capacity of slope
            slope.append(input()) # Cost of slope

        slopes.append(slope)
        slopesReorder = reorder(slopes)
        tree = buildTree(slopesReorder)
    #     capacity, cost = solve(tree)
    #
    #     print("Case #%i: %s %s" % (caseNum, capacity, cost))