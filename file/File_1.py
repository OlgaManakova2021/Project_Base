f1 = open('new_file_1.txt', 'r', encoding="utf-8")
print('Читаем и выводим на экран первые 10 байт или символов')
print(f1.read(30))
f1.close()

f1 = open('new_file_1.txt', encoding="utf-8")
print('Читаем и выводим на экран весь файл')
print(f1.read())
f1.close()

f1 = open('new_file_1.txt', encoding="utf-8")
print('Читаем и выводим на экран весь файл с помощью for')
for line in f1:
    print(line, end='')
print(type(f1.read()))
f1.close()


