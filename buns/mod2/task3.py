input_str = input()
current = ''
current_number = 0
a = 0
b = 0
c = 0

for i in input_str:
    if i != ' ':
        current += i
    elif current_number == 0:
        current_number += 1
        a = float(current)
        current = ''
    elif current_number == 1:
        current_number += 1
        b = float(current)
        current = ''
c = float(current)

if a > b > c or a < b < c:
    print(b)
elif b > a > c or c > a > b:
    print(a)
else:
    print(c)
