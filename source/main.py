import tree

# Read in lines in order starting from 1 (root of slopes)

def reorder(slopes): # List of lists, where each list contains starting pt, ending pt, capacity, and cost
    slopeCount = 0
    restPoint = 1
    newSlopes = []
    while (slopeCount < len(slopes)):
        for slope in slopes:
            if (slope[0] == restPoint):
                newSlopes.append(slope)
                restPoint = slope[1]
                slopeCount += 1
                break
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
    exit(1)
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
        capacity, cost = solve(tree)

        print("Case #%i: %s %s" % (caseNum, capacity, cost))


# tree = tree.Tree()
# tree.setRoot(1)
# print(tree.insert(1, 2, 2, 5))
# print(tree.insert(1, 3, 2, 5))
# print(tree.insert(3, 4, 1, -2))
# node = tree.get(3)
# print(node)
# print(node.getID())
# node2 = node.getChildren()
# for n in node2:
#     print(n.getCapacity())
#     print(n.getCost())