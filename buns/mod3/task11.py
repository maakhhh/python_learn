winners = ""
line = input()
length = len(line)
map = [line]
for i in range(length - 1):
    line = input()
    map.append(line)

if any([map[i] == "X"*length for i in range(length)]): winners += "X"
if any(map[i] == "O"*length for i in range(length)): winners += "O"

for i in range(length):
    if [map[j][i] for j in range(length)].count("X") == length: winners += "X"
    if [map[j][i] for j in range(length)].count("O") == length: winners += "O"

if length % 2 == 1:
    if [map[i][i] for i in range(length)].count("X") == length: winners += "X"
    if [map[i][length - 1 - i] for i in range(length)].count("X") == length: winners += "X"
    if [map[i][i] for i in range(length)].count("O") == length: winners += "O"
    if [map[i][length - 1 - i] for i in range(length)].count("O") == length: winners += "O"

result = set(winners)
print("Ничья" if len(result) == 2 else winners[0])


