L = [1, 3, 2, 5, 20, 21]

# список целых чисел, которые нужно возвести в квадрат
print(list(map(lambda x: x**2, L)))

#отфильтровать, оставив четные числа
print(list(filter(lambda x: x % 2 == 0, L)))

from functools import reduce
print(reduce(lambda x,y: y-x, L)) # работа reduce
                                  # 3 - 1 = 2
                                  # 2 - 2 = 0
                                  # 5 - 0 = 5
                                  # 20 - 5 = 15
                                  # 21 - 15 = 6
