#1 Структура базы данных с телефонными номерами
# phonebook = {}
# phonebook['Mark'] = 8956214587
# phonebook['Tom'] = 8956214587
# phonebook['Tim'] = 8956214587
#
# print(phonebook)

#2 Пример структуры базы данных с особым типом инициализации
# phonebook = {
#     'Mark': 5623457896,
#     'Tom': 5784512365,
#     'Timotee': 457812563
# }
#
# print(phonebook)

#3 Синтаксис по перебору словарей
# phonebook = {
#     'Mark': 5623457896,
#     'Tom': 5784512365,
#     'Timotee': 457812563
# }
#
# for name, phone in phonebook.items():
#     print("%s имеет номер телефона %d" % (name, phone))

#4 Синтаксис по удалению некоторого значения (пример 1)
# phonebook = {
#     'Mark': 5623457896,
#     'Tom': 5784512365,
#     'Timotee': 457812563
# }
#
# print(f'Исходный словарь: {phonebook}')
#
# del phonebook['Mark']
#
# print(f'Измененный словарь: {phonebook}')


#5 Синтаксис по удалению некоторого значения (пример 2)
phonebook = {
    'Mark': 5623457896,
    'Tom': 5784512365,
    'Timotee': 457812563
}

print(f'Исходный словарь: {phonebook}')

phonebook.pop('Mosk', 'не существует!') # в консоль ни чего не выведется

print(f'Измененный словарь: {phonebook}')

#6 Синтаксис встроенной функции dict()
# managers_ages = dict(Andrew = 27, Lara = 35, Nick = 37)
# print(managers_ages)

#7 Синтаксис совместной работы методов словарей
# managers_ages = dict({'Andrew': 27, 'Lara': 35}, Nick = 37)
# print(managers_ages)

#8 Синтаксис с использованием несуществующего ключа
# population = {
#     'Berlin': 3842569,
#     'Hamburg': 456891,
#     'Munich': 457896,
# }
#
# print(population['Mosc'])

#9 Синтаксис с использованием несуществующего ключа + default
# population = {
#     'Berlin': 3842569,
#     'Hamburg': 456891,
#     'Munich': 457896,
# }
#
# print(population.get("Mosc", 'Не существует!'))

#10 Синтаксис использования встроенной функции dict.get()
# population = {
#     'Berlin': 3842569,
#     'Hamburg': 456891,
#     'Munich': 457896,
# }
#
# print(f'Популяция Берлина {population.get("Berlin")}')

#11 Синтаксис команды для добавления элемента в словарь
# population = {
#     'Berlin': 3842569,
#     'Hamburg': 456891,
#     'Munich': 457896,
# }
#
# print(f'Исходный словарь: {population}')
#
# population['Rostov'] = 1500000
#
# print(f'Измененный словарь: {population}')

#12 Синтаксис использования функции dict.update()
# phonebook = {
#     'Mark': 5623457896,
#     'Tom': 5784512365,
#     'Timotee': 457812563
# }
#
# print(f'Исходный словарь: {phonebook}')
#
# phonebook.update(Max = 457812367, Tim = 789564123)
#
# print(f'Измененный словарь: {phonebook}')


#ДЗ № 1
# sample = {
#     'Name': 'David',
#     'Surname': 'Backham',
#     'email': 'david_b@gmail.com',
# }
#
# print(f'Исходный словарь: {sample}')
#
# sample.pop('Name')
# sample.pop('Surname')
#
# print(f'Измененный словарь: {sample}')

#ДЗ № 2
# sample = {
#     'Name': 'David',
#     'Surname': 'Backham',
#     'email': 'david_b@gmail.com',
# }
#
# print(f'Исходный словарь: {sample}')
#
# print(f'Значение параметра email: {sample.get("email")}')