import abc
from queue import (
    SimpleQueue,
    Queue,
    PriorityQueue,
    LifoQueue
)
from typing import (
    List,
    Any,
    Optional
)


class QuickSortAbstractClass(abc.ABC):

    @abc.abstractmethod
    def _partition(self):
        pass

    @abc.abstractmethod
    def _concatenate(self):
        pass
    
    @abc.abstractmethod
    def _sort(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass


class SequenceBasedQuickSort(QuickSortAbstractClass):
    """ Quick Sort for a sequence implemented as queue"""

    def __init__(self, sequence: Any):
        if not (type(sequence) in [Queue, SimpleQueue, PriorityQueue, LifoQueue]):
            raise TypeError(f'{sequence} does not belong to any of the python queue class')
        self.sequence: Any = sequence

    def _partition(self, pivot: int, sequence: Queue, lesser: Queue, equal: Queue, greater: Queue):
        value: Optional[int] = None
        while not sequence.empty():
            value = sequence.get()
            if value < pivot:
                lesser.put(value)
            elif value > pivot:
                greater.put(value)
            else:
                equal.put(value)

    def _concatenate(self, sequence: Any, lesser: Queue, equal: Queue, greater: Queue):
        while not lesser.empty():
            sequence.put(lesser.get())
        while not equal.empty():
            sequence.put(equal.get())
        while not greater.empty():
            sequence.put(greater.get())

    def _sort(self, sequence: Any):
        if sequence.qsize() < 2: return

        pivot: int = sequence.get()

        # queue for holding values less than the pivot
        lesser: Queue = Queue()
        # queue for holding values equal to the pivot
        equal: Queue = Queue()
        # queue for holding values greater than the pivot
        greater: Queue = Queue()

        # because the first value of the self.sequence is chosen as the pivot, we need to put that value into the E queue
        equal.put(pivot)
    
        self._partition(pivot, sequence, lesser, equal, greater)
        self._sort(lesser)
        self._sort(greater)
        self._concatenate(sequence, lesser, equal, greater)

    
    def run(self):
        self._sort(self.sequence)
        return list(self.sequence.queue)

class InplaceQuickSort(QuickSortAbstractClass):
    """Quick Sort for an array based sequence using inplace algorithm"""

    def __init__(self, sequence: List):
        if not(type(sequence) == list):
            raise TypeError(f'{sequence} should be a python list')

        self.sequence: List = sequence
        self.left: Optional[int] = None
        self.right: Optional[int] = None 
    

    def _partition(self, sequence: List, pivot: int, pivot_index: int, left: int, right: int):
        while left <= right:
            while left <= right  and sequence[left] < pivot:
                left += 1
            while left <= right and sequence[right] > pivot:
                right -= 1
            if left <= right:
                sequence[left], sequence[right] = sequence[right], sequence[left]
                left, right = left + 1, right - 1
        sequence[left], sequence[pivot_index] = sequence[pivot_index], sequence[left]
        self.left, self.right = left, right

    def _concatenate(self):
        pass

    def _sort(self, sequence: List, leftmost_index, rightmost_index):
        if leftmost_index >= rightmost_index: return
        
        pivot: int = sequence[rightmost_index]

        left, right = leftmost_index, rightmost_index - 1

        self._partition(sequence, pivot, rightmost_index, left, right)
        self._sort(sequence, leftmost_index, self.left - 1)
        self._sort(sequence, self.left + 1, rightmost_index)

    
    def run(self):
        leftmost_index, rightmost_index = 0, len(self.sequence) - 1
        self._sort(self.sequence, leftmost_index, rightmost_index)
        return self.sequence

if __name__ == '__main__':
    random_list: List = [2,6,7,1,10,3,3,5,9,8,4,4,5,6]
    # Running Queue based Sequence quick sort
    input_sequence: Queue = Queue()
    for value in random_list:
        input_sequence.put(value)
    result: List = SequenceBasedQuickSort(input_sequence).run()
    print(result)

    # Running Array based Sequence quick sort using inplace algorithm
    output = InplaceQuickSort(random_list).run()
    print(output)