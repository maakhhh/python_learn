def evklid(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        return evklid(a - b, b) if a > b else evklid(a, b - a)


a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
print(f"НОД = {evklid(a, b)}")