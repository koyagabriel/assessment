class Tree:
    def __init__(self):
        self.root = None

    def to_object(self):
        return self.root

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return
        current = self.root
        while(True):
            if current.value > value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    return


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        