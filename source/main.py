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
    for slope in slopes:
        newTree.insert(slope[0], slope[1], slope[2], slope[3])
    return newTree

def solve(tree):
    costList = tree.calculate()
    capacity, cost = tree.maxCapMinCost(costList)
    return capacity, cost

if __name__ == "__main__":
    testCases = int(input())
    for caseNum in range(1, testCases + 1):
        slopes = []
        restPoints = int(input())
        for restPoint in range(1, restPoints):
            slope = list(map(int, input().split())) # Slope starting rest point, ending rest point, capacity, cost
            slopes.append(slope)
        slopesReorder = reorder(slopes)
        tree = buildTree(slopesReorder)
        exit(1)
        capacity, cost = solve(tree)
        print("Case #%i: %s %s" % (caseNum, capacity, cost))