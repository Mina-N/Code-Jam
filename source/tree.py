class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NoRoot(Error):
    """Exception raised for a tree with no root.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

class NoNodeFound(Error):
    """Exception raised for a tree without desired node

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

class NoCost(Error):
    """Exception raised when trying to find cost of a tree with only a root

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class Node:

    def __init__(self, id, capacity = None, cost = None):
        self.children = None
        self.id = id
        self.capacity = capacity
        self.cost = cost

    def setID(self, id):
        self.id = id

    def setCapacity(self, capacity):
        self.id = capacity

    def setCost(self, cost):
        self.cost = cost

    def setChildren(self, children):
        self.children = children

    def getID(self):
        return self.id

    def getCapacity(self):
        return self.capacity

    def getCost(self):
        return self.cost

    def getChildren(self):
        return self.children


class Tree:

    def __init__(self):
        self.root = None

    def setRoot(self, id):
        self.root = Node(id)
        return True

    def insert(self, id_source, id_dest, capacity, cost):
        if (self.root == None):
            return self.setRoot(id_source)
        else:
            return self.insertNode(self.root, id_source, id_dest, capacity, cost)

    def insertNode(self, currentNode, id_source, id_dest, capacity, cost):
        if (currentNode.id == id_source):
            if (currentNode.getChildren() == None):
                children = []
                children.append(Node(id_dest, capacity, cost))
                currentNode.setChildren(children)
            else:
                children = currentNode.getChildren()
                children.append(Node(id_dest, capacity, cost))
                currentNode.setChildren(children)
            return True
        if (currentNode.getChildren() == None):
            return
        for child in currentNode.getChildren():
            success = self.insertNode(child, id_source, id_dest, capacity, cost)
            if (success):
                return success
        return False

    def get(self, id_source):
        if (self.root == None):
            raise NoRoot("Tree does not contain root.")
        try:
            return self.getNode(self.root, id_source)
        except NoNodeFound as fail:
            return fail.message


    def getNode(self, currentNode, id_source):
        if (currentNode.getID() == id_source):
            return currentNode
        if (currentNode.getChildren() == None):
            return
        for child in currentNode.getChildren():
            node = self.getNode(child, id_source)
            if (node):
                return node
        raise NoNodeFound("Tree does not contain desired node.")

    def calculate(self):
        if (self.root == None):
            raise NoRoot("Tree does not contain root.")
        try:
            startList = []
            parents = []
            return self.calculateCost(self.root, startList, 0, 1000, parents)
        except NoCost as fail:
            return fail.message

    # Traversal method to find the cost of paths and minimum capacity for every node from the root.
    # Returns list of nodes, costs, and capacities.

    def calculateCost(self, currentNode, costList, cost, minCapacity, parents): # will only find sum of costs of one path with leaf
        if (currentNode.getChildren() == None):
            if (currentNode.getID() == 1):
                raise NoCost("Root does not have cost.")
            newParents = list(parents)
            costList.append((currentNode.getID(), cost, minCapacity, newParents))
            return costList
        if (currentNode.getID() != 1):
            newParents = list(parents)
            costList.append((currentNode.getID(), cost, minCapacity, newParents))

        newParents = list(parents)
        newParents.append(currentNode.getID())
        parents = newParents

        for child in currentNode.getChildren():
            if (child.getCapacity() < minCapacity):
                minCapacity = child.getCapacity()
            costList = self.calculateCost(child, costList, cost + child.getCost(), minCapacity, parents)

        return costList

# tree = Tree()
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
# listCosts = tree.calculate()
# print(listCosts)

# tree = Tree()
# tree.setRoot(1)
# print(tree.insert(1, 3, 5, 5))
# print(tree.insert(1, 4, 2, -1))
# print(tree.insert(3, 2, 3, -2))
# print(tree.insert(3, 5, 2, -1))
# print(tree.insert(3, 6, 2, 2))
# print(tree.insert(4, 7, 2, 2))
# listCosts = tree.calculate()
# print(listCosts)
