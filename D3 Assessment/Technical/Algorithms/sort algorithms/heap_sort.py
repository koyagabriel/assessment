from typing import (
    List,
    Any
)

class HeapSort:
    """Sort list of comparable elements into nondecreasing order."""
    def __init__(self, sequence: List):
        if not(type(sequence) == list):
            raise TypeError(f'{sequence} should be a python list')
        self.sequence: List = sequence

    def _heapify(self, sequence: List, index: int, length: int):
        largest: int = 2 * index + 1
        while largest <= length:
            if (largest < length) and (sequence[largest] < sequence[largest + 1]):
                largest += 1

            if sequence[largest] > sequence[index]:
                sequence[largest], sequence[index] = sequence[index], sequence[largest]
                index = largest
                largest = 2 * index + 1
            else:
                return

    def _sort(self, sequence: List):
        length: int = len(sequence) - 1
        least_parent: int = length // 2
        for i in range(least_parent, -1, -1):
            self._heapify(sequence, i, length)

        for i in range(length, 0, -1):
            if sequence[0] > sequence[i]:
                sequence[i], sequence[0] = sequence[0], sequence[i]
                self._heapify(sequence, 0, i - 1)

    def run(self):
        self._sort(self.sequence)
        return self.sequence

if __name__ == '__main__':
    random_list: List = [12, 11, 13, 50, 5, 6, 7]
    print(HeapSort(random_list).run())
