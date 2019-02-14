# Search Algorithms

### Breadth First Search

The breadth first search algorithm is a method of searching through data in graph or tree data structures and it basically involves starting at the root node and traversing the tree by finding the nearest neighbours first, then going one depth deeper into another node.

It finds the shortest path from a given source vertex to all other vertices. It transverses breadthwards, starting from vertices that are of distance K from the source vertex, then moves to vertices that of distance K + 1 and so forth. It is applied in 
1. Dijkstra Algorithm,
2. Garbage Collection,
3. Parsing Social Graphs such as connection between people in LinkedIn and Facebook,
4. Networking: Open Shortest Path First concept when routing packets from one network to another.

### A* Search
It is used for pathfinding and graph transversal. It is an informed search algorithm, meaning it is formulated in terms of weighted graphs. It aims at finding the shortest path/ path with the smallest cost (least distance travelled and shortest time) to a goal node from a source node.

A* search is a combination of Djikstra's and Best First Search algorithms. It uses the sum of 'cost' (distance from source to the current node, defined by g(n)) as well as 'heuristic' (estimated distance from current node to destination, defined by h(n)). 

What makes A* different and better for many searches is that for each node, A* uses a function  that gives an estimate of the total cost of a path using that node.
```
                            f(n) = g(n) + h(n)
where

 f(n) = total estimated cost of path through node n

 g(n) = cost so far to reach node n

 h(n) = estimated cost from n to goal.

```

The pseudocode for the A* algorithm is presented with Python-like syntax.
```
make an openlist containing only the starting node
   make an empty closed list
   while (the destination node has not been reached):
       consider the node with the lowest f score in the open list
       if (this node is our destination node) :
           we are finished 
       if not:
           put the current node in the closed list and look at all of its neighbors
           for (each neighbor of the current node):
               if (neighbor has lower g value than current and is in the closed list) :
                   replace the neighbor with the new, lower, g value 
                   current node is now the neighbor's parent            
               else if (current g value is lower and this neighbor is in the open list ) :
                   replace the neighbor with the new, lower, g value 
                   change the neighbor's parent to our current node

               else if this neighbor is not in both lists:
                   add it to the open list and set its g
```

### Depth First Search
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

Depth-first search is useful for testing a number of properties of graphs, including whether there is a path from one vertex to another and whether or not a graph is connected. It is also applied in searching for solutions in artificial intelligence or web-crawling.

 <h1 style="text-align: center; text-decoration: underline">SORTING ALGORITHMS</h1>

<h2>Quick Sort</h2>
Quick Sort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. Like merge-sort, this algorithm is also based on the divide-and-conquer paradigm, but it uses this technique in a somewhat opposite manner, as all the hard work is done before the recursive calls.

<h4 style="text-align: center;">High-Level Description of Quick-Sort</h4>

The quick-sort algorithm sorts a sequence **S** using a simple recursive approach. The main idea is to apply the **divide-and-conquer** technique, whereby we divide **S** into subsequences, recur to sort each subsequence, and then combine the sorted subsequences by a simple concatenation.
In particular, the quick-sort algorithm consists of the following three steps:

   1. **Divide:** If **S** has at least two elements (nothing needs to be done if **S** has zero or one element), select a specific element **x** from **S**, which is called the **pivot**.
   Remove all the elements from **S** and put them into three sequences:

      - **L**, storing the elements in S less than x.
      - **E**, storing the elements in S equal to x.
      - **G**, storing the elements in S greater than x.
   
     Of course, if the elements of S are distinct, then E holds just one element the pivot itself.

   2. **Conquer:** Recursively sort sequences L and G.
   3. **Combine:** Put back the elements into S inorder byfirst inserting the elements of L, then those of E, and finally those of G.



<h4 style="text-align: center;">Performing Quick Sort on Queue based Sequences</h4>

This implementation of quick sort works on any sequence type that operates as a queue. This implementation chooses the first item of the queue as the pivot and then it divides sequence **S** into queues **L**, **E**, and **G** of elements that are respectively less than, equal to, and greater than the pivot. We then recur on the **L** and **G** lists, and transfer elements from the sorted lists **L**, **E**, and **G** back to **S**

[Click on me to view code for Quick-Sort on Queue based sequences](https://github.com/koyagabriel/assessment/blob/299f5706f47d5a567b56c1b5e7e468a2c7d75a6a/D3%20Assessment/sort%20algorithms/quick_sort.py#L34)

<h4 style="text-align: center;">Additional Optimizations for Quick-Sort using Inplace Algorithm</h4>

An algorithm is in-place if it uses only a small amount of memory in addition to that needed for the original input. The implementation of quick-sort above does not qualify as in-place because we used additional containers L, E, and G when dividing a sequence S within each recursive call. Quick-sort of an array-based sequence can be adapted to be in-place.
In this algorithm, we use the input sequence itself to store the subsequences for all the recursive calls.

[Click on me to view code for Quick-Sort using Inplace Algorithm.](https://github.com/koyagabriel/assessment/blob/299f5706f47d5a567b56c1b5e7e468a2c7d75a6a/D3%20Assessment/sort%20algorithms/quick_sort.py#L86)

----------



<h2>Merge Sort</h2>

Merge Sort make use of recursion in an algorithm design pattern called **divide and conquer**

<h4 style="text-align: center;">High-Level Description of Merge Sort</h4>

To sort a sequence **S** with **n** elements using the three divide-and-conquer steps, the merge-sort algorithm proceeds as follows:
1. **Divide:** If **S** has zero or one element, return **S** immediately; it is already sorted. Otherwise (**S** has at least two elements), remove all the elements from **S** and put them into two sequences, **S1** and **S2**, each containing about half of the elements of **S**; that is, **S1** contains the first <b>n/2</b> elements of **S**, and **S2** contains the remaining **[n/2]** elements.
2. **Conquer:** Recursively sort sequences **S1** and **S2**.
3. **Combine:** Put back the elements into **S** by merging the sorted sequences **S1**
and **S2** into a sorted sequence.

<h4 style="text-align: center;">Array-Based Implementation of Merge-Sort</h4>

We begin by focusing on the case when a sequence of items is represented as an ***(array-based)*** Python list. The merge function is responsible for the subtask of merging two previously sorted sequences, **S1** and **S2**, with the output copied into **S**. We copy one element during each pass of the while loop, conditionally determining whether the next element should be taken from **S1** or **S2**.

[Click on me to view code for Array-Based Implementation of Merge-Sort](https://github.com/koyagabriel/assessment/blob/2ef05f77e487928d056c912587d4392f25351471/D3%20Assessment/sort%20algorithms/merge_sort.py#L29)

<h4 style="text-align: center;">Alternative Implementations of Merge-Sort using Python Queue</h4>

The merge-sort algorithm can also easily be adapted to use any form of a basic queue as its container type.

[Click on me to view code for Queue-Based Implementation of Merge-Sort](https://github.com/koyagabriel/assessment/blob/2ef05f77e487928d056c912587d4392f25351471/D3%20Assessment/sort%20algorithms/merge_sort.py#L68)


# HASHING ALGORITHMS
A hashing algorithm is a cryptographic hash function. It is a mathematical algorithm that maps data of arbitrary size to a hash of a fixed size. It’s designed to be a one-way function, infeasible to invert.

The ultlimate goal of a hashing algorithm is to generate a safe hash.
**(A hash is a value computed from a base input number using a hashing algorithm)**.

Shortly, the hash value is a summary of the original data. For instance, think of a paper document that you squeeze and squeeze so that, in the end, you aren’t even able to read the content. It’s almost (in theory) impossible to restore the original input without knowing what was the starting data.

### Qualities of an ideal cryptographic hash function
1. It should be fast to compute the hash value for any kind of data.
2. It should be impossible to regenerate a message from its hash value.
3. It should avoid hash collisions, each message has its own hash.
4. Every change to a message, even the smallest one, should change the hash value. It should be completely different. It’s called the `avalanche effect`.


### What we use it for?
1. Digital Signatures.
2. Message authentication codes (MACs).
3. Identifying Files (used in `.lock files` for uniquely identifying packages).
4. Detecting duplicates or as checksums `(detecting if a file didn't suffer accidental or intentional data corruption)`.


#### MD5(Message Digest Algorithm)
It is a widely used hash function producing 128-but hash value. Although MD5 was initially designed to be used as a cryptographic hash function, it has been found to suffer from extensive vulnerabilities such as supporting **collision**. It can still be used as a checksum to verify data integrity, but only against unintentional corruption. It remains suitable for other non-cryptographic purposes, for example for determining the partition for a particular key in a partitioned database.

#### Collision
A collision or clash is a situation that occurs when two distinct pieces of data have the same hash value.


#### Linear Probing
Linear probing is a scheme in computer programming for resolving collisions in hash tables, data structures for maintaining a collection of key–value pairs and looking up the value associated with a given key. In these schemes, each cell of a hash table stores a single key–value pair. When the hash function causes a collision by mapping a new key to a cell of the hash table that is already occupied by another key, linear probing searches the table for the closest following free location and inserts the new key there.

In linear probing, we linearly probe for next slot. Example
```
If slot hash(x) % S is full, then we try (hash(x) + 1) % S
If (hash(x) + 1) % S is also full, then we try (hash(x) + 2) % S
If (hash(x) + 2) % S is also full, then we try (hash(x) + 3) % S 
```
