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



# Create traversal method for tree to find the cost of paths for every leaf from the root and rank in ascending order
# Return list of nodes and paths in order

# Create method to find minimum capacity for each unique node path
# Return minimum capacity

# Create method to find cost of path given minimum capacity
# Return cost of path