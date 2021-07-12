# Найти факториал произвольного целого числа.
k = input("Введите число для расчета факториала: ")

while type(k) != int:  # обработка исключений
    try:
        k = int(k)
    except ValueError:
        print("Неправильно ввели!")
        k = input("Введите число: ")

s = 1
while k:
    s *= k
    k -= 1
print (s)