class LinkedList:
    def __init__(self):
        self.head = self.tail =  None
        self.length = 0

    def push(self, value):
        node = Node(value)
        self.length += 1
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def pop(self):
        return self.delete(self.length  - 1)

    def _test(a, b):
        return a == b

    def _find(self, value, test=_test):
        current = self.head
        counter = 0
        while(current):
            if (test(value, current.value, counter)):
                return current
            current = current.next
            counter += 1
        return None   

    def _test_index(self, search, _current, i):
        return search == i

    def get(self, index):
        node = self._find(index, self._test_index)
        if not node: return None
        return node.value

    def delete(self, index):
        if index == 0: 
            head = self.head
            if head:
                self.head = head.next    
            else:
                self.tail = self.head = None
            self.length -= 1
            return head.value

        node = self._find(index - 1, self._test_index)
        excise = node.next
        if not excise: return None
        node.next = excise.next
        if node.next and not node.next.next:
            self.tail = node.next

        self.length -= 1
        return excise.value
        



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(5)
    linked_list.push(1)
    print(linked_list.get(1))

