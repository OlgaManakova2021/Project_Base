def cylinder():
    r = float(input("Введи радиус: "))
    h = float(input("Введи высоту: "))
    side = 2 * 3.14 * r * h
    circle = 3.14 * r ** 2
    full = side + 2 * circle
    return side, full, circle

print('Площадь')
sCyl, fCyl, cir = cylinder()     # side, full
print("Площадь боковой поверхности: %.2f" % sCyl)
print("Полная площадь фигуры: %.2f" % fCyl)
print("Площадь круга: %.2f" % cir)


