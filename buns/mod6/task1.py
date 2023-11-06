class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None
        self.iter = self.start

    def push(self, val):
        new_node = Node(val)
        if self.start is None:
            self.start = new_node
            self.iter = self.start
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = new_node

    def get(self, index):
        current = self.start
        for i in range(index):
            current = current.next
        return current.value

    def remove(self, index):
        pre_current = self.start
        for i in range(index - 1):
            pre_current = pre_current.next
        post_current = pre_current.next.next
        pre_current.next = post_current

    def insert(self, n, val):
        new_value = Node(val)
        current = self.start
        for i in range(n - 1):
            current = current.next
        next_current = current.next
        new_value.next = next_current
        current.next = new_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter is not None:
            val = self.iter.value
            self.iter = self.iter.next
            return val
        else:
            raise StopIteration
