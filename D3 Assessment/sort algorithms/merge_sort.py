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


class MergeSortAbstractClass(abc.ABC):

    @abc.abstractmethod
    def _merge(self):
        pass

    @abc.abstractmethod
    def _sort(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

class ArrayBasedMergeSort(MergeSortAbstractClass):
    """Merge sort implementation for array based sequence such as a python list"""

    def __init__(self, sequence: List):
        if not(type(sequence) == list):
            raise TypeError(f'{sequence} should be a python list')

        self.sequence: List = sequence

    def _merge(self, left_sequence: List, right_sequence: List, sequence: List):
        i = j = 0

        while i + j < len(sequence):
            if j == len(right_sequence) or (i < len(left_sequence) and left_sequence[i] < right_sequence[j]):
                sequence[i+j] = left_sequence[i]
                i += 1
            else:
                sequence[i+j] = right_sequence[j]
                j += 1


    def _sort(self, sequence: List):

        length_of_sequence: int = len(sequence)
        if length_of_sequence < 2: return

        mid: int = length_of_sequence // 2
        left_sequence: List = sequence[0:mid]
        right_sequence: List = sequence[mid:length_of_sequence]

        self._sort(left_sequence)
        self._sort(right_sequence)

        self._merge(left_sequence, right_sequence, sequence)

    def run(self):
        self._sort(self.sequence)
        return self.sequence

class QueueBasedMergeSort(MergeSortAbstractClass):
    """Merge sort implementation for queue based sequence"""

    def __init__(self, sequence: Any):
        if not (type(sequence) in [Queue, PriorityQueue, LifoQueue]):
            raise TypeError(f'{sequence} does not belong to any of the python queue class [Queue, PriorityQueue, LifoQueue]')
        self.sequence: Any = sequence

    def _merge(self, sequence: Any, left_sequence: Queue, right_sequence: Queue):
        """Merge two sorted queue instances left_sequence and right_sequence into empty queue sequence"""
        while not left_sequence.empty() and not right_sequence.empty():
            if list(left_sequence.queue)[0] < list(right_sequence.queue)[0]:
                sequence.put(left_sequence.get())
            else:
                sequence.put(right_sequence.get())
            
        while not left_sequence.empty():
            sequence.put(left_sequence.get())
        
        while not right_sequence.empty():
            sequence.put(right_sequence.get())

    def _sort(self, sequence):
        size: int = sequence.qsize()

        if size < 2: return
     
        left_sequence: Queue = Queue()
        right_sequence: Queue = Queue()

        # move the size//2 elements to left_sequence
        while left_sequence.qsize() < size//2:
            left_sequence.put(sequence.get())
        # move the rest to right_sequence
        while not sequence.empty():
            right_sequence.put(sequence.get())

        self._sort(left_sequence)
        self._sort(right_sequence)

        self._merge(sequence, left_sequence, right_sequence)

    def run(self):
        self._sort(self.sequence)
        return list(self.sequence.queue)


if __name__ == '__main__':
    random_list: List = [2,6,7,1,10,3,3,5,9,8,4,4,5,6]

    # Running Array based Sequence merge sort using inplace algorithm
    output: List = ArrayBasedMergeSort(random_list).run()
    print(output)

    # Running Queue based Sequence merge sort
    input_sequence: Queue = Queue()
    for value in random_list:
        input_sequence.put(value)
    
    result: List = QueueBasedMergeSort(input_sequence).run()
    print(result)
