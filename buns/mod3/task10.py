size = int(input())

matrix = [[i for i in range(1, size + 1)] for j in range(size)]
for i in matrix:
    print(", ".join(map(str, i)))
print()
for i in range(size):
    print(", ".join(map(str, [matrix[j][i] for j in range(size)])))