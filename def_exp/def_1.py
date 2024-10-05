# программа выводит SOS

# # объявление функции CharS()
# def CharS():
#     print('S', end='\t')
#
# # объявление функции CharO()
# def CharO():
#     print('O', end='\t')
#
# # вызов функции CharS()
# CharS()
#
# # вызов функции CharO()
# CharO()
#
# # вызов функции CharS()
# CharS()

# def my_oper():
#     print("Сумма чисел = ", 120 + 80)
#     print("Произведение чисел = ", 14 * 5)
#     print("Разность чисел = ", 17 - 5)
#
# my_oper()

# def my_sum(a_func, b_func):
#     print("Сумма чисел = ", a_func + b_func)
#
# a = int(input("Введи число a: "))
# b = int(input("Введи число b: "))
# my_sum(a, b)

# def my_prod(a, b):
#     print('Произведение чисел = ', a*b)
#     print('Сумма чисел = ', a + b)
#     print('Разница чисел = ', a - b)
#     print('Степень числа = ', a ** b)
#
# a = int(input("Введи а: "))
# b = int(input("Введи b: "))
# my_prod(a, b)

# def my_prod(a, b):
#     return a * b
#
# a = int(input("Введи а: "))
# b = int(input("Введи b: "))
# print('Произведение чисел = ', my_prod(a, b))

# def my_oper(a, b, c):
#     return a*b*c
#
# a = int(input("Введи а: "))
# b = int(input("Введи b: "))
# c = 3
# print('Произведение чисел = ', my_oper(a, b, c))

# def my_oper(a, b, c):
#     if a == b:
#         return a*c
#     else:
#         return b*c
#
# a = int(input("Введи а: "))
# b = int(input("Введи b: "))
# c = 6
# print('Произведение чисел = ', my_oper(a, b, c))

# var1 = "Глобальная"
# def my_func():
#     global var2
#     var2 = "Локальная"
#     print(var2)
#     print(var1)
# print(var1)
# my_func()
# print(var2)


# var1 = "Глобальная"
# def func():
#     global var1, var3
#     var2 = "Локальная"
#     var3 = "Еще одна локальная переменная"
#     print(var2)
#     var1 = 234
#     print(var1)
#
# print(var1)
# func()
# print(var1)
# print(var3)

# Составить функцию определения количества цифр в
# целом числе
# 456 => 3

# def countInt(k):    # k = 456
#     t = 0
#     while k > 0:
#         k //= 10    # 4 // 10 = 0
#         t += 1      #  t = 3
#     return t
#
# Int_Nuber = int(input("Введи целое число: "))
# print('Количество цифр в числе:   ', countInt(Int_Nuber))
