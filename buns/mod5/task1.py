class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None


class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        val = self.end
        self.end = self.end.pref
        return val

    def push(self, val):
        new_value = Node(val)
        new_value.pref = self.end
        self.end = new_value

    def print(self):
        val = self.end
        while val is not None:
            print(val.data, end=" ")
            val = val.pref
        print('\n')
