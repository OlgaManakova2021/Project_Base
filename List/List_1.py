# Дан целочисленный массив размера N. Увеличить все четные числа,
# содержащиеся в массиве, на исходное значение последнего четного числа.
# Если четные числа в массиве отсутствуют, то оставить массив без изменений.

import random


def PrintList(ListAppend):
    for element in ListAppend:
        print(element, end=' ')
    print()


d = int(input('Введи размер массива:   '))
ListAppend = []
t = 0
while t < d:
    ListAppend.append(random.randint(-100, 100))
    if ListAppend[t] % 2 == 0:
        k = ListAppend[t]
    t += 1

print('Исходный массив', sep='\n')
PrintList(ListAppend)
print('Последнее четное число:  ', k, sep='\n')
for i in range(len(ListAppend)):
    if ListAppend[i] % 2 == 0:
        ListAppend[i] += k

print('Полученный список', sep='\n')
PrintList(ListAppend)
