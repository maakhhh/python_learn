class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        val = self.start.data
        self.start = self.start.pref
        return val

    def push(self, val):
        new_value = Node(val)
        if self.start is None:
            self.start = new_value
            self.end = new_value
        else:
            self.end.pref = new_value
            new_value.nref = self.end
            self.end = new_value

    def insert(self, n, val):
        new_value = Node(val)
        first = self.start
        for i in range(n - 2):
            first = first.pref
        second = first.pref
        new_value.nref = first
        new_value.pref = second
        first.pref = new_value
        second.nref = new_value

    def print(self):
        val = self.start
        while val is not None:
            print(val.data, end=" ")
            val = val.pref
        print("\n")
