print('Запишем в файл структуру данных - список')
lst = [' tree', ' four']
f2 = open('data.txt', 'w')
f2.write('one')
f2.write(' two')
f2.writelines(lst)
f2.close()

f2 = open('data.txt')
print(f2.read())
print(type(f2.read())) # получаем тип - строка
f2.close()
