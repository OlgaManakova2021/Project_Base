# name = "Olga"           # str
# print("Переменная name до изменения: ", name)
# surname = 'Manakova'    # str
# print(type(surname))
# print(type(name))
#
# # # print(name)
# # # print(surname)
# #
# name = 145              # int
# print("Переменная name после изменения: ", name)
# print(type(name))
#
# flt = 15.35             # float
# print(type(flt))
#
# bln = True              # bool
# print(type(bln))
#
# bln_1 = False           # bool

# cmp = 3+2j              # complex
# print(type(cmp))
# cmp_1 = 6-5j            # complex
# print(cmp_1)

# a = int(input("Введи переменную а:  "))
# b = int(input("Введи переменную b:  "))
# sum = a + b
# print("Переменная а:", a)
# print("Переменная b:", b)
# print(sum)
# print(type(a), type(b))
#
# c = float(input("Введи переменную c:  "))
# print("Переменная с: ", c)
# print(type(c))

# a = str(input("Введите первую переменную   "))
# b = int(input("Введите вторую переменную   "))
# c = float(input("Введите третью переменную  "))
#
# print("Тип:", type(a), "Значение :", a)
# print("Тип:", type(b), "Значение :", b)
# print("Тип:", type(c), "Значение :", c)

# a = int(input("Введите первую переменную   "))
# b = float(input("Введите вторую переменную   "))
# c = int(input("Введите третью переменную   "))
# result = a + b + c
# print("Сумма = ", result)

# print(not False)
# print(not True)
#
# print(True and True)        # True
# print(True and False)       # False
# print(False and True)       # False
# print(False and False)      # False

# print(True or True)        # True
# print(True or False)       # True
# print(False or True)       # True
# print(False or False)      # False
#
# a = int(input("Введи целое число  "))
# if a > 0:
#     print("Ваше число больше 0")
#     print("Программа завершена")
#     print("Пока!")
# else:
#     print("Ваше число меньше или равно 0")
#     print("Программа завершена еще раз!!!!")



# d = len(c)
# print(d)

# if len(b) > len(c):
#     print("Первый список длиннее")
# else:
#     print("Второй список длиннее")

# print(abs(-15))
# print(abs(-15.75))

# print(chr(97))
# print(chr(112))
# print(chr(98))
#
# print(ord('ю'))
# print(ord('ц'))
# print(ord("ъ"))

# print(float('45.36'))
# print(type(float('45.36')))
# print(float(78))

# print(help(input))
# print(help(print))

# max_b = max(b)
# print("Максимальный элемент списка b = ", max_b)
# max_c = max(c)
# print("Максимальный элемент списка c = ", max_c)
# #
# print("Минимальный элемент списка b = ", min(b))
# print("Минимальный элемент списка c = ", min(c))

# print(list(reversed(b)))
# print(list(reversed(c)))

# print(list(range(10, 20)))
# print(list(range(10, 20, 2)))
# print(list(range(10, 25, 3)))
# print(list(range(100, 200, 20)))

# print(sorted(b))
# print(sorted(c))

# b = [1, 20, 3]
# c = [10, 120, 30, 40]
# print("Сумма элементов списка b = ", sum(b))
# print("Сумма элементов списка с = ", sum(c))

# Используя встроенные функции max() и sum(),
# найдите максимальное значение в последовательности x = [1, 3, 5, 10, 11]
# и посчитайте сумму элементов в последовательности y = [10, 55, 12, 100].

# x = [1, 3, 5, 10, 11]
# y = [10, 55, 12, 100]
# print("Максимальное значение x = ", max(x))
# print("Сумма элементов y = ", sum(y))

# Используя встроенные функции min() и reversed(),
# необходимо найти минимальное значение в последовательности a = [-2, 0, 4, 8, 10] и
# развернуть порядок элементов в последовательности b = [6, 4, 2, 0].

# a = [-2, 0, 4, 8, 10]
# b = [6, 4, 2, 0]
# print("минимальное значение в последовательности a = ", min(a))
# print("Обратный порядок элементов b ", list(reversed(b)))

# n = []
# print(len(n), type(n))

# flt = [45.77, 12.12, -98.65]
# suf = [6, 'for', 47.22, False]
# print(flt)
# print(suf)
# suf_1 = [6, [2, 3, 4],'for', 47.22, False]
# print(suf_1)

# n_1 = list()
# print(len(n_1), type(n_1))

# q = list(input("Введите элементы списка  "))
# print(q)
# print(len(q))

# z_1 = "слово"
# lst = list(z_1)
# print(lst)

# b = [6, 7, -8, 0] * 3
# str = ["abs", 'int', 'float'] * 5
# print(b)
# print(str)

# b = [16, 7, -8, 70]
# print(b[2], b[3], b[0], b[3])
# print(b[-1])
# print(b[-3], b[-4])
# b[2] = 18
# print(b)
# b[1] = 100
# print(b)

# rex, tob, puth = elem
# print(rex)
# print(tob)
# print(puth)

# elem = ['Рекс', "Тобик", "Пушок"]
# print("Цикл For")
# for i in elem:
#     print(i)

# elem = ['Рекс', "Тобик", "Пушок", 45, 102, 78, 45, 56]
# print("Цикл While")
# i = 0
# while i < len(elem):
#     print(elem[i])
#     i += 1

# elem = ['Рекс', "Тобик", "Пушок"]
# elem_1 = ['Рекс', "Тобик", "Пушок"]
# # print(elem == elem_1)
# if elem == elem_1:
#     print("Списки равны")
# else:
#     print("Списки не равны")

# a = 3
# while a < 8:
#     print("Результат = ", a**2)
#     a += 1
#     if a == 6:
#         break

# a = 3
# while a < 8:
#     print("Результат = ", a**2)
#     a += 1
#     if a == 6:
#         continue

# for i in range(15, 26):
#     print(f"Итерация {i} = ", i)







