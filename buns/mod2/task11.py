input_str = input()
currents = ''
result = False

for i in input_str:
    if i != ' ':
        if i in currents:
            result = True
            break
        currents += i
print(result)