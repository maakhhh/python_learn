input_str = input()

gl = 'ёуеыаоэюи'
sg = 'йцкнгшщзхфвпрлджчсмтб'

count_gl = 0
count_sg = 0

for i in input_str:
    if i in gl:
        count_gl += 1
    elif i in sg:
        count_sg += 1

print(count_gl, count_sg)