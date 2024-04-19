# unsorted_dict = {'фрукт': 'яблоко', 'цвет': 'антрацит', 'артикул': 'в5678',
#                  'модель': 'бабочка', 'наименование': 'книга', 'жанр': 'триллер'}
# print(dict(sorted(unsorted_dict.items(), key=lambda item: item[1])))

# def prod(lst):
#     prod = 1
#     for i in lst:
#         prod *= i
#     return prod
#
# lst = list(map(int, input("введи через элементы списка:  ").split()))
# print(prod(lst))

# import math
# lst = list(map(int, input("введи через элементы списка:  ").split()))
# print(math.prod(lst))

# from functools import reduce
# lst = list(map(int, input("введи через элементы списка:  ").split()))
# print(reduce(lambda x, y: x * y, lst))

# ops = {'neg': lambda x: abs(x), 'pos': lambda x: x / 2, 'zero': lambda x: x + 5}
# lst = list(map(int, input("введи через пробел длину списка и его элементы:  ").split()))
# for i in lst:
#     if i < 0:
#         print(ops['neg'](i))
#     elif i > 0:
#         print(ops['pos'](i))
#     else:
#         print(ops['zero'](i))

# ops = [(lambda x, y: x + y), (lambda x, y: x - y),
#        (lambda x, y: x * y), (lambda x, y: x / y)]
#
# x, y = int(input("Введи x: ")), int(input("Введи y:  "))
# for i in range(len(ops)):
#     print(ops[i](x, y))

# def get_min_or_max(value='max'):
#     return eval(f'lambda x: {value}(x)')
#
# lst = [3, 5, -22, -15, 100, 7, 8, 9, 12, 98]
#
# max_func = get_min_or_max()
# min_func = get_min_or_max('min')
# print(max_func(lst))
# print(min_func(lst))

# numbers = [7, 8, 6, 9, 4, -6, 2, 0, -3, -12, -5, -2, 12, 77, 32]
# print(list(filter(lambda x: x > 6 and x % 2 == 0, numbers)))

# st = 'яжертыуиопшщасдфгчйклзхцвбнм'
# vowels = 'аиеёоуыэюя'
# result = list(map(lambda x: 'гласная' if x in vowels else 'согласная', st))
# print(result)

# def my_function(n):
#  	return lambda a : a * n
#
# double = my_function(2)
# print(double(15))
