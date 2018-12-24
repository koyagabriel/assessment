'''
Implementing a list in python which is also know as ArrayList in javascript.
This kind of data structure is index based and gets values by specifying an index.
This form of data structure optimizes the get process of an element, while 
deoptimizing both the delete and insert process of an element.

The get process is optimized because it only needs the index where the element is
stored which is like a memmory location identifier, making it faster to fetch.

The delete process is deoptimized because after deleting an element from an index, it
needs to shift the remaining elements on the right to the left, in order to fill in the
blank index where an element was deleted from. This functionality gets expensive as the
list increases in size.

The insert process is similar to the delete process because you will need to shift the elements
right in order to free up the index where you want to insert the element.
'''

class List:
    def __init__(self):
        self.length = 0
        self.data = []

    def __str__(self):
        return str(self.data)

    def push(self, value):
        self.data += [value]
        self.length += 1 #we increment the lenght, so that we can insert the next passed value into the next slot

    def pop(self):
        # we return the element at the last index and delete the index.
        return self.delete(self.length - 1)

    def delete(self, index):
        answer = self.data[index] # we fetch the element at the passed in index
        self._collapse_to(index) # we shift the remaining element to the right left
        return answer # we return the fetched element

    def get(self, index):
        return self.data[index] # we simply return the element at the index passed in as argument

    def _collapse_to(self, index):
        for i in range(index, self.length-1): # we generate the list of indexes of the remaining element to the right, using the index passed in as the start point
            self.data[i] = self.data[i + 1] # we move each elements position to the left by one
        else:
            del self.data[self.length - 1]
            self.length -= 1 # we set the new length of the list, which will be one lesser than it's previous length.

        
test_list = List()
test_list.push(4)
test_list.push(5)
test_list.push(6)
test_list.push(7)
test_list.push(8)

print(f'After pushing: {test_list}')

print(test_list.pop())
print(f'After poping: {test_list}')

print(test_list.delete(0))
print(f'After delete: {test_list}')

print(f'After getting: {test_list.get(2)}')

