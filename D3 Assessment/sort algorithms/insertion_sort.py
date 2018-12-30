from typing import (
    List,
    Any
)

class InsertionSort:
    """Sort list of comparable elements into nondecreasing order."""
    def __init__(self, sequence: List):
        if not(type(sequence) == list):
            raise TypeError(f'{sequence} should be a python list')
        self.sequence: List = sequence
    
    def _sort(self, sequence: List):
        for index in range(1, len(sequence)):
            current_element: Any = sequence[index]
            j: int = index
            while (j > 0) and (sequence[j-1] > current_element):
                sequence[j] = sequence[j-1]
                j -= 1
            sequence[j] = current_element

    def run(self):
        self._sort(self.sequence)
        return self.sequence

if __name__ == '__main__':
    random_list: List = [2,6,7,1,10,3,3,5,9,8,4,4,5,6]

    # Running Array based Sequence merge sort using inplace algorithm
    output: List = InsertionSort(random_list).run()
    print(output)
