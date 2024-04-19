import random

lst = []
n = int(input('Введи размер массива'))


table = [
    [x * y for x in range(3, 8)]
    for y in range(3, 8)]
print(table)



n = int(input('Введи размер массива'))
a, b = [], []
t = 0
while t < n:
    a.append(random.randint(1, 2))
    t += 1
print('Исходный массив', a, sep='\n')
t = 0
i = 0
while t < n:
    s = 0
    while i < n:
        s += a[i]
        i += 1
    b.append(s / (n - t))
    t += 1
    i = t
print(b)