#ввести 4 числа. найти количество четных и нечетных чисел.

a1 = int(input("Введи число:   "))
a2 = int(input("Введи число:   "))
a3 = int(input("Введи число:   "))
a4 = int(input("Введи число:   "))

count_even = 0 #четные
count_odd = 0 #нечетные

# % - взятие остатка от деления

if a1 % 2 == 0:
    count_even += 1
else:
    count_odd += 1

if a2 % 2 == 0:
    count_even += 1
else:
    count_odd += 1

if a3 % 2 == 0:
    count_even += 1
else:
    count_odd += 1

if a4 % 2 == 0:
    count_even += 1
else:
    count_odd += 1

print("Количество нечетных чисел = ", count_odd)
print("Количество четных чисел = ", count_even)




#ввести 4 числа. найти количество положительных четных и отрицательных нечетных чисел.

