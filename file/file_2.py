print('Запишем в файл структуру данных - список')
l = [' tree', ' four']
f2 = open('data.txt', 'w')
f2.write('one')
f2.write(' two')
f2.writelines(l)
f2.close()
f2 = open('data.txt')
print(f2.read())
print('получаем тип', type(f2.read()))
f2.close()

# содержимое файла data_2.txt:
# зима
# весна
# лето
# осень

nums = []
for i in open('data_2.txt', encoding='UTF-8'):
    nums.append(i[:-1])
print(nums)
print('получаем тип', type(nums))

