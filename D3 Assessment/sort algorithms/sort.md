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