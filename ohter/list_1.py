# Программа запрашивает с клавиатуры пять чисел, добавляет их в список.
# На экран выводит их сумму, максимальное и минимальное из них.

ListAppend = []
i = 0
while i < 5:
    ListAppend.append(int(input('Введи значение списка:  ')))
    i += 1
print(ListAppend)
print('Сумма элементов списка:   ', sum(ListAppend))
print('Минимальный элемент списка:   ', min(ListAppend))
print('Максимальный элемент списка:   ', max(ListAppend))