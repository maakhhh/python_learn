input_str = input()
last = ''
result = ''

for i in input_str:
    if i == ' ':
        result += last
    last = i
result += last

print(result)