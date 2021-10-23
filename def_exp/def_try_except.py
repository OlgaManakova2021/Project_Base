# вывод положительных четных чисел в обратном порядке от заданного числа
import logging

logging.basicConfig(filename="../dict/sample5.log", level=logging.INFO)
log = logging.getLogger("ex")

def try_except(d):
    while type(d) != int:  # обработка исключений
        log.exception('Запуск программы')
        try:
            d = int(d)
            return d
        except ValueError:
            log.exception(f"ValueError")
            print("Неправильно ввели!")
            d = input("Введите целое число: ")


t = input("Введите целое число: ")

t = try_except(t)

while t:  # обработка чисел
    t -= 1
    if t % 2 != 0: continue
    print(t, end=' ')
print()
# print('Программа успешно завершена!')
log.exception('Программа успешно завершена')