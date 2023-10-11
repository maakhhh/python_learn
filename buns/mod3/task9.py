n = int(open("input.txt").readline())

steps = 2
current = 2
pos = [0, 0]

for i in range(n):
    if current == 0:
        steps += 2
        current = steps
    step = -1 if (steps//2) % 2 == 1 else 1
    pos = [pos[0] + step * (current > (steps // 2)), pos[1] + step * (current <= (steps // 2))]
    current -= 1

open("output.txt", "w").write(" ".join(map(str, pos)))

