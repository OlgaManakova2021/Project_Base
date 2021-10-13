# Дан список размера N, состоящий из символов. Привести символы букв
# из верхнего регистра в нижний. Определить количество букв.

import random
import List_def as l1

List_4 = []
d = int(input('Введи размер массива:   '))

t = 0
while t < d:
    List_4.append(chr(random.randint(45, 100)))
    t += 1

print('Исходный массив:   ')
l1.PrintList(List_4)

h = 0
for i in List_4:
    if i.isalpha():
        h += 1

print('Количество букв:   ', h)


New_String = ''.join(List_4) # преобразование списка в строку
print("Переводим буквы в нижний регистр:   ", New_String.lower())

