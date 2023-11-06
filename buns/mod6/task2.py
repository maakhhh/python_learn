class DoubleElement:
    def __init__(self, *lst):
        self.list = [i for i in lst]
        if len(self.list) % 2 == 1:
            self.list.append(None)
        self.start = 0
        self.end = 2

    def __next__(self):
        start = self.start
        end = self.end
        if end > len(self.list):
            raise StopIteration
        self.start += 2
        self.end += 2
        return self.list[start : end]

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)

