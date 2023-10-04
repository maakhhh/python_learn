input_str = input()
current = ''
a = 0
b = 0

for i in range(len(input_str)):
    if input_str[i] != ',' and input_str[i] != ' ':
        current += input_str[i]
    else:
        a = float(current)
        b = float(input_str[i + 2:])
        break
print(a % b)