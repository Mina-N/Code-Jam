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
        return(self.id)

    def getCapacity(self):
        return(self.capacity)

    def getCost(self):
        return(self.cost)

    def getChildren(self):
        return(self.children)


class Tree:

    def __init__(self):
        self.root = None

    def setRoot(self, id):
        self.root = Node(id)

    def insert(self, id_source, id_dest, capacity, cost):
        if (self.root == None):
            self.setRoot(id_source)
        else:
            self.insertNode(self.root, id_source, id_dest, capacity, cost)

    def insertNode(self, currentNode, id_source, id_dest, capacity, cost):
        if (currentNode.id != id_source):
            if (currentNode.getChildren() != None):
                for child in currentNode.getChildren():
                    self.insertNode(child, id_source, id_dest, capacity, cost)
            else:
                return(False)

        if (currentNode.getChildren() == None):
            children = []
            children.append(Node(id_dest, capacity, cost))
            currentNode.setChildren(children)
        else:
            children = currentNode.getChildren()
            children.append(Node(id_dest, capacity, cost))
            currentNode.setChildren(children)

        return(True)

    def get(self, id_source):
        if (self.root == None):
            return(False)
        self.getNode(self.root, id_source)

    def getNode(self, currentNode, id_source):
        if (currentNode.getID() != id_source):
            if (currentNode.getChildren() != None):
                for child in currentNode.getChildren():
                    self.getNode(child, id_source)
            else:
                return(False)

        return(currentNode)


tree = Tree()
tree.setRoot(7)

# Create traversal method for tree to find the cost of paths for every node from the root and rank in ascending order
# Return list of nodes and paths in order

# Create method to find minimum capacity for each unique node path
# Return minimum capacity

# Create method to find cost of path given minimum capacity
# Return cost of path