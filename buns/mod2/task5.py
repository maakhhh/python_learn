input_str = input()
alph = 'abcdefghijklmnopqrstuvwxyz'
i = input_str[:1]
n = int(input_str[2:])
index_i = 0

for j in range(len(alph)):
    if alph[j] == i:
        index_i = j

index = (index_i + n) % 26

print(alph[index])