# def func1(): ...
# func1()     #	При вызове ничего не делает

# вывод положительных четных чисел в обратном порядке от заданного числа

t = input("Введите целое число: ")

while type(t) != int: # обработка исключений
    try:
        t = int(t)
    except ValueError:
      print("Неправильно ввели!")
      t = input("Введите целое число: ")

while t: # обработка чисел
    t -= 1
    if t % 2 != 0: continue
    print(t, end=' ')
print()
print('Программа успешно завершена!')


# while True:
#     name = input('Enter name: ')
#     if name == 'stop': break
#     age = input ('Enter age: ')
#     print('Hello', name, '=>', int(age) ** 2)
