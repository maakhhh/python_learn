input_str = input()
result = ''

for i in input_str:
    if i not in '-() ':
        result += i
print(result)