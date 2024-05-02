#отфильтровать, оставив нечетные числа
# print(list(filter(lambda x: x % 2 != 0, L)))
#

# def foo(x):
#     return x**4
#
# print(foo(4))


# def foo(a, b, c):
#     global x
#     return a * b * c
#
# x, y, z = int(input()), int(input()), int(input())
# print(foo(x, y, z))


# global a, b
#
# def foo(a, b):
#     return a - b
#
# x, y = int(input()), int(input())
# print(foo(x, y))
#
# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# print(new_list)
#
# current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(map(lambda x: x*2 , current_list))
# print(new_list)
#
# from functools import reduce
# current_list = [5, 15, 20, 30, 50, 55, 75, 60, 70]
# summa = reduce((lambda x, y: x + y), current_list)
# print(summa)
#
# tables = [lambda x = x: x*10 for x in range(1, 11)]
# for table in tables:
#     print(table())
#
# max_number = lambda a, b: a if a > b else b
# print(max_number(3, 5))
#
# current_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
# sorted_list = lambda x: (sorted(i) for i in x)
# second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
# result = second_largest(current_list, sorted_list)
# print(result)

# x = [1,3,5,10,11]
# print("Максимальный = ", max(x))
# print("Сумма = ", sum(x))

# x = [1,3,5,10,11]
# print("Минимальный = ", min(x))
# print("Обратный порядок = ", list(reversed(x)))

# x = [3,7,2,5,10]
# print(sum(i**3 for i in x))


# a = [3,6,8,10]
# b = [11,15,25,32]
# print(min(max(a),min(b)))

# Домашка
# Задача 1
#Используя встроенную функцию abs(), вывести на консоль абсолютные значения чисел:

# print(abs(-5.2))
# print(abs(-4.7))
# print(abs(0))

#Задача 2
#используя встроенную фукнцию enumerate(), пронумеровать следующие слова

string_one = "Строка"
for i in enumerate(string_one):
    print(i)

string_two = "Python"
for i in enumerate(string_two):
    print(i)

string_two = "Hello"
for i in enumerate(string_two):
    print(i)

capitals = dict()
capitals['Rus'] = 'Moskow'
capitals['USA'] = 'Wosh'

