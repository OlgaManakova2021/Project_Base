# Дан массив A размера N. Сформировать новый массив B того же размера по следующему правилу:
# элемент BK равен среднему арифметическому элементов массива A с номерами от K до N

import random

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
