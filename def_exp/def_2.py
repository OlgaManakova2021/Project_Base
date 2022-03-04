def rectangle():
    """Вычисление площади прямоугольника"""
    a = float(input("Ширина %s: " % figure)) # обращение к глобальной
    b = float(input("Высота %s: " % figure)) # переменной figure
    return print("Площадь: %.2f" % (a*b))

def triangle():
    """Вычисление площади треугольника

    Используется общепринятая формула

    """
    a = float(input("Основание %s: " % figure))
    h = float(input("Высота %s: " % figure))
    return print("Площадь: %.2f" % (0.5 * a * h))

figure = input("1-прямоугольник, 2-треугольник: ")
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(rectangle.__doc__)
