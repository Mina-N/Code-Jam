from modules import tree

# Read in lines in order starting from 1 (root of slopes)

def reorder(slopes): # List of lists, where each list contains starting pt, ending pt, capacity, and cost
    pass

def buildTree(slopes):
    pass

def solve(tree):
    pass


if __name__ == "__main__":

    testCases = input()

    for caseNum in range(1, testCases + 1):
        slopes = []
        restPoints = input()
        for restPoint in range(1, restPoints + 1):
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