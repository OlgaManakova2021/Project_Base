# Найти все двузначные числа, в которых есть заданная цифра. Реализовать с применением функции.

def search_figure(k):
    d = 10
    while d != 100:
        a, b = divmod(d, 10)
        if (a == k) or (b == k):
            print(d, -d)
        d += 1


figure = input("Введи целое число от 0 до +- 9: ")

while type(figure) != int:  # обработка исключений
    try:
        figure = int(figure)
    except ValueError:
        print("Неправильно ввели!")
        figure = input("Введите целое число: ")

search_figure(figure)
