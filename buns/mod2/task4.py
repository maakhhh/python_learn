input_str = input()

try:
    if int(input_str) != float(input_str):
        print('Неверный ввод')
except:
    print('Неверный ввод')

n = int(input_str)
n2 = ''
n8 = ''
n16 = ''

while n > 0:
    n2 = str(n % 2) + n2
    n = n // 2

n = int(input_str)

while n > 0:
    o = n % 8
    n8 = str(o) + n8
    n = n // 8

n = int(input_str)

digits = "0123456789ABCDEF"

while n > 0:
    o = n % 16
    digit = digits[o]
    n16 = digit + n16
    n //= 16

print(f'{n2}, {n8}, {n16}')