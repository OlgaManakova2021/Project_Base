def duble(a, b):
    ploch = a * b
    perim = 2 * (a + b)
    return ploch, perim

g_ploch, g_perim = duble(a=2, b=5)
print('Площадь прямоугольника:  ', g_ploch)
print('Периметр прямоугольника:  ', g_perim)
