input_str = input()

sum_ch = 0
sum_nc = 0

for i in range(len(input_str)):
    if i % 2 == 0:
        sum_nc += int(input_str[i])
    else:
        sum_ch += int(input_str[i])

print('yes' if (sum_ch*3 + sum_nc) % 10 == 0 else 'no')