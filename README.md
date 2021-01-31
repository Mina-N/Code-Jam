# Code-Jam


An implementation of the successive shortest paths algorithm in Python using Tree and Node classes. The first input to the algorithm is the number of test cases. For each test case, the input consists of the number of nodes (n) and n-1 edges described via four integers: the edge's starting node, the edge's ending node, the maximum number of units the edge can accommodate, and the edge's cost per unit. There is only one path to each node from the root node (labeled 1). The algorithm works as follows:

(1) Find the path costs to all the nodes using any tree traversal from the root while calculating the cost of each node as the cost of its parent plus the cost of the edge connecting them. 
(2) Store the paths in a list and sort them in ascending order based on cost.
(3) Compute the minimum capacity of the first path (the least costly path) in the list. Add the minimum capacity to a running sum of the capacity of the tree and calculate the cost of traversing the path by multiplying the minimum capacity by the path cost.
(4) Update the capacities of each parent node in the path. Keep in mind that a path with a minimum capacity of zero can no longer be traversed.
(5) Repeat steps (3) and (4) until all paths in the list have been traversed. 

The output of the algorithm is the test case number, the maximum capacity or number of units that the tree can sustain, and the minimum cost of sustaining that number of units.
