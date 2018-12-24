# ALGORITHMS

## Linear Search
In computer science, linear search or sequential search is a method for finding a target value within a list. It sequentially checks each element of the list for the target value until a match is found or until all the elements have been searched. Linear search runs in at worst linear time and makes at most n comparisons, where n is the length of the list. <br /><br />
An algorithm is said to take linear time, or O(n) time, if its time complexity is O(n). Informally, this means that the running time increases at most linearly with the size of the input. More precisely, this means that there is a constant c such that the running time is at most `cn` for every input of size n. For example, a procedure that adds up all elements of a list requires time proportional to the length of the list, if the adding time is constant, or, at least, bounded by a constant.

### Linear Search Algorithm
Linear search sequentially checks each element of the list until it finds an element that matches the target value. If the algorithm reaches the end of the list, the search terminates unsuccessfully.

#### Basic algorithm
Given a list L of n elements with values or records L0 .... Ln−1, and target value T, the following subroutine uses linear search to find the index of the target T in L. <br /><br />

```
Set index to 0.
If Li = T, the search terminates successfully; return i.
Increase i by 1.
If i < n, go to step 2. Otherwise, the search terminates unsuccessfully.
```
https://github.com/koyagabriel/assessment/blob/master/algorithms/linear%20search/basic_linear_search.py

#### With a sentinel
The basic algorithm above makes two comparisons per iteration: one to check if Li equals t, and the other to check if i still points to a valid index of the list. By adding an extra record Ln to the list (a sentinel value) that equals the target, the second comparison can be eliminated until the end of the search, making the algorithm faster. The search will reach the sentinel if the target is not contained within the list.

```
Set index to 0.
If Li = T, go to step 4.
Increase i by 1 and go to step 2.
If i < n, the search terminates successfully; return i. Else, the search terminates unsuccessfully.
```
https://github.com/koyagabriel/assessment/blob/master/algorithms/linear%20search/linear_search_with_sentinel.py

#### In an ordered table
If the list is ordered such that L0 ≤ L1 ... ≤ Ln−1, the search can establish the absence of the target more quickly by concluding the search once Li exceeds the target. This variation requires a sentinel that is greater than the target.

```
Set i to 0.
If Li ≥ T, go to step 4.
Increase i by 1 and go to step 2.
If Li = T, the search terminates successfully; return i. Else, the search terminates unsuccessfully.
```
https://github.com/koyagabriel/assessment/blob/master/algorithms/linear%20search/linear_search_on_ordered_list.py

## Binary search
Binary search works on sorted arrays. Binary search begins by comparing the middle element of the array with the target value. If the target value matches the middle element, its position in the array is returned. If the target value is less than or greater than the middle element, the search continues in the lower or upper half of the array, respectively, eliminating the other half from consideration. <br /><br />
Binary search is a fast search algorithm with run-time complexity of Ο(log n). This search algorithm works on the principle of divide and conquer. For this algorithm to work properly, the data collection should be in the sorted form.

```
Given an array A of n elements with values or records A0, A1, ..., An−1, sorted such that A0 ≤ A1 ≤ ... ≤ An−1, and target value T, the following subroutine uses binary search to find the index of T in A.

Set L to 0 and R to n − 1.
If L > R, the search terminates as unsuccessful.
Set m (the position of the middle element) to the floor, or the greatest integer less than (L + R) / 2.
If Am < T, set L to m + 1 and go to step 2.
If Am > T, set R to m − 1 and go to step 2.
Now Am = T, the search is done; return m.
```
https://github.com/koyagabriel/assessment/blob/master/algorithms/binary_search.py

## Dijkstra Algorithm
Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.<br /><br />
For example, if the nodes of the graph represent cities and edge path costs represent driving distances between pairs of cities connected by a direct road, Dijkstra's algorithm can be used to find the shortest route between one city and all other cities. As a result, the shortest path algorithm is widely used in network routing protocols, most notably IS-IS (Intermediate System to Intermediate System) and Open Shortest Path First (OSPF).
