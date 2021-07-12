def duble(a, b):
    ploch = a * b
    perim = 2 * (a + b)
    return ploch, perim


# width = float(input('Введи ширину:   '))
# height = float(input('Введи высоту:   '))
g_ploch, g_perim = duble(b=20, a=10)
print('Площадь прямоугольника:  ', g_ploch)
print('Периметр прямоугольника:  ', g_perim)
