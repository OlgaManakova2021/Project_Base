# вывод положительных четных чисел в обратном порядке от заданного числа
def try_except(d):
    while type(d) != int:  # обработка исключений
        try:
            d = int(d)
            return d
        except ValueError:
            print("Неправильно ввели!")
            d = input("Введите целое число: ")


t = input("Введите целое число: ")

t = try_except(t)

while t:  # обработка чисел
    t -= 1
    if t % 2 != 0: continue
    print(t, end=' ')
print()
print('Программа успешно завершена!')
