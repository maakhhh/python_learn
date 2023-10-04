input_str = input()

n0 = 0
n1 = 0

for i in input_str:
    if i == '0':
        n0 += 1
    else:
        n1 += 1

if n0 == n1:
    print('yes')
else:
    print('no')