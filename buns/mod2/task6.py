input_str = input()

current = ''

for i in input_str[::-1]:
    if i != '.':
        current += i
    else:
        print(current[::-1])
        current = ''
print(current[::-1])