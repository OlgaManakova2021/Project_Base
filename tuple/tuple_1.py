# tuplex = (4, 6, 2, 8, 3, 1)
# print(tuplex)

# tuplex = tuplex + (9,)
# print(tuplex)
# print(*tuplex)
#
#
#
# x = (5, 10, 15, 20)

# print(type(x))
# y = reversed(x)
# print(tuple(y))
# print(type(y))
#
# a, b, *c = tuplex
# print(a,b,c)
# f = a + b
# print(f)


# Нахождение максимума из трех чисел
# var max := a > b ? a : b;
# max := c > max ? c : max;

a = 50
b = 100
c = 40
max = a if a > b else b
max = c if c > max else max
print(max)

# Дано целое число. Если оно является положительным,
# то прибавить к нему 20, в противном случае вычесть из него 5/
# Результат сохраняется

c = int(input('Введи число:     '))
f = c + 20 if c >= 0 else c - 5
print('Результат =  ', f)

# print(len(c))


