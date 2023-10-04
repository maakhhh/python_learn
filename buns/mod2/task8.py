input_str = input()
count = 0

s = ''

for i in input_str:
    if i != ',':
        s += i
    else:
        break

ii = input_str[-1]

for i in input_str:
    if i == ii:
        count += 1
    else:
        break

print(count)