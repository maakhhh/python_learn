name = input()
f = open(name)
chars = {}

for i in f:
    for j in i:
        if "a" <= j <= "z" or "A" <= j <= "Z" or "а" <= j <= "я" or "А" <= j <= "Я":
            if j in chars.keys():
                chars[j] += 1
            else:
                chars[j] = 1

f = open("output.txt", "w")

for i in sorted(chars, reverse=True):
    f.write(f"{i}: {chars[i]}\n")