# допускается также
# использовать две
# целочисленные переменные j и k

from random import randint

a = []
n = 20

for i in range(0, n):
    a.append(randint(-10, 10))

print(a)

max = a[0]

for i in range(0, n):
    if (a[i] % 3 != 0) and (a[i] > max):
        max = a[i]

print(max)
