def pal(word):
    chars = {}
    count_evens = 0
    side = ""
    middle = ""
    for i in word:
        if i in chars.keys():
            chars[i] += 1
        else:
            chars[i] = 1
    for (key, value) in chars.items():
        if value % 2 == 1:
            if len(word) % 2 == 0 or count_evens != 0:
                return False
            middle = key * value
            count_evens += 1
        else:
            side += key * (value // 2)

    return side + middle + side[::-1]


word = input()
print(pal(word))
