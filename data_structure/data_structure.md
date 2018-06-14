# GRAPH

A graph is made up of two components, which are the vertex and edges. The vertex represents the entities, while the edges represent the relationships. In a neural network computation graph, the vertices are called neurons, while the edges are the data the flow in the neurons and are called tensors.
https://github.com/koyagabriel/assessment/blob/master/data_structure/graph-algorithms/graph.py

## Types of Graph

- Directed graphs refers to a one way relationship between vertices (entities) in the graph. An example is 'Jim drives his Car`. The relationship is only directed in one way which is from Jim to the car, because Jim drives the Car, but the car cannot drive Jim. An arrow is used to denote this relationship.

- Undirected graph on the other hand is a bi-directional relationship. That is, relationship exist in both ways. An example is Jim and Joe play ball. In this case the relationship flows both ways. In this kind of graph, an arrow isn't use to denote the relationship.

The number of edges connected to a vertex(node) in a graph is known as the degree of the node. Edges that flow into a vertex(node) determines the in-degree of the vertex, while edges that flows out (emanate) of that vertex, determines the out-degree of that vertex.

### Three ways to represent graphs in code are

- Adjacency matrices (https://github.com/koyagabriel/assessment/blob/master/data_structure/graph-algorithms/adjacency_matrix.py)
- Adjacency lists
- Adjacency sets (https://github.com/koyagabriel/assessment/blob/master/data_structure/graph-algorithms/adjacency_set.py)

### They are two ways of traversing Graphs

- Breadth-first search. (https://github.com/koyagabriel/assessment/blob/master/data_structure/graph-algorithms/breadth_first.py)
- Depth-first search. (https://github.com/koyagabriel/assessment/blob/master/data_structure/graph-algorithms/depth_first.py)

Breadth-first simply means all nodes at the same distance from origin are visited together, while Depth-first means all nodes in certain direction from origin are visited together.


# TREE

A graph which has all its node connected but has no cycle is called a Tree. A Tree always has a root node, which forms the ancestoral node for that tree. A tree will always have all its node connected. A set of disjoint trees is called a forest. It simply means having multiple trees not connected together.

### Binary tree

In a binary tree each node can have at most 2 children, because each node can have at most children, the left node is called the left child and the other is called the right child. For nodes that have only one child, the other node can be null.

#### Binary Search Tree (https://github.com/koyagabriel/assessment/blob/master/data_structure/binary_search_tree.py)

A binary search tree is a binary tree that is, every parent node must have at most 2 children. There is a specific rule for how the values associated with each node are arranged. BSTs are sorted so every value on the left of a particular node is smaller than it and every value on the right of a particular node is larger than it. Because BSTs have this structure we can do operations like search, insert and delete pretty quickly.

#### B-Trees

A B-tree is a self-balancing tree data structure that keeps data sorted and allows searches, sequential access, insertions, and deletions in logarithmic time. B-tree is well suited for storage systems that read and write relatively large blocks of data, such as discs. It is commonly used in databases and filesystems.

#### Heaps

A heap is a specific type of tree with some of its own additional rules. In a heap elements are arranged in increasing or decreasing order such that the root element is either the maximum or minimum value in a tree.

##### Types of heaps: Max heaps and Min heaps

In a Max heap a parent must always have a greater value than its child so the root ends up being the biggest element. The opposite is true of Min heaps, a parent has a lower value than its child so the root is the minimum element. Heaps do not need to be binary tree so parent can have any number of children.
