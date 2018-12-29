# Quick Sort
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. Like merge-sort, this algorithm is also based on the divide-and-conquer paradigm, but it uses this technique in a somewhat opposite manner, as all the hard work is done before the recursive calls.

### High-Level Description of Quick-Sort
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

### Performing Quick Sort on Queue based Sequences
This implementation of quick sort works on any sequence type that operates as a queue. This implementation chooses the first item of the queue as the pivot and then it divides sequence **S** into queues **L**, **E**, and **G** of elements that are respectively less than, equal to, and greater than the pivot. We then recur on the **L** and **G** lists, and transfer elements from the sorted lists **L**, **E**, and **G** back to **S**

[Click on me to view code for Quick-Sort on Queue based sequences](https://github.com/koyagabriel/assessment/blob/299f5706f47d5a567b56c1b5e7e468a2c7d75a6a/D3%20Assessment/sort%20algorithms/quick_sort.py#L34)

### Additional Optimizations for Quick-Sort using Inplace Algorithm.
An algorithm is in-place if it uses only a small amount of memory in addition to that needed for the original input. The implementation of quick-sort above does not qualify as in-place because we used additional containers L, E, and G when dividing a sequence S within each recursive call. Quick-sort of an array-based sequence can be adapted to be in-place.
In this algorithm, we use the input sequence itself to store the subsequences for all the recursive calls.

[Click on me to view code for Quick-Sort using Inplace Algorithm.](https://github.com/koyagabriel/assessment/blob/299f5706f47d5a567b56c1b5e7e468a2c7d75a6a/D3%20Assessment/sort%20algorithms/quick_sort.py#L86)

