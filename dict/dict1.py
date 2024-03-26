# a = {'cat': 'кошка', 'dog': 'собака', 'bird': 'птица', 'mouse': 'мышь'}
# print(a)
# for key in a:
#     print(key, '->', a[key])


# Программа формирует словарь, состоящий из уникальных символов и их повторений в
# заданном предложении
# s_n = {}
# for i in 'Изучаем язык программирования Питон':
#     if i not in s_n:
#         s_n[i] = 1
#     else:
#         s_n[i] += 1
# print (s_n)
# for i in s_n.items():
#     print(i)

# a = [['cat','кошка'], ['dog','собака'], ['bird','птица'], ['mouse','мышь']]
# s = dict(a)
# print(s)

# t = dict.fromkeys(['a','b','c'],15)
# print(t)

# Программа преобразует в словарь значения из строки
# t = 0
# student = {}
# inf = 'Иванов Иван Иванович ПОКС-29 5 3 5 5 4'
# inf = inf.split()
# student['Фамилия'] = inf[0]
# student['Имя'] = inf[1]
# student['Отчество'] = inf[2]
# student['Группа'] = inf[3]
# student['Оценки'] = []
# for i in inf[4:]:
#     student['Оценки'].append(int(i))
# print(student)


#Добавить в словарь новый элемент elephant = слон, если его еще нет в словаре
# a = {'cat': 'кошка', 'dog': 'собака', 'bird': 'птица', 'mouse': 'мышь'}
# if 'elephant' not in a:
#     a['elephant'] = 'слон'
# print(a)

# a = {'cat': 'кошка', 'dog': 'собака', 'bird': 'птица', 'mouse': 'мышь'}
# a.popitem()
# print(a)
# a.popitem()
# print(a)


# Cities = ['Moscow', 'Sr.Petersburg', 'Vladimir']
# City = {x: y for y, x in enumerate(Cities, start=100)}
# print(City)
#
# Population = [17201245, 4520196, 3124075]
# DICT = {x: y for x, y in zip(Cities, Population)}
# print(DICT)


# Cities = {
#              'Moscow': 1,
#              'St.Petersburg': 2,
#              'Vladimir': 3,
#              'Rostov': 4
# }
# Cities['Omsk'] = 5
# Cities['Nowosib'] = 6
#
# print(Cities)

# Office = {
#     'Mark': 1,
#     'John': 2,
#     'Mathew': 3,
#     'Ben': 4,
#     'Lark': 5
# }
# print(Office)
#
# del Office['Ben']
# del Office['Lark']
# print(Office)

#
# Phonebook = {
#               'Mark': 89451258842,
#              'John': 89457852852,
#              'Mathew': 84957841254,
#              'Ben': 84956384571,
#              'Lark': 84956397845
# }
#
# for name, number in Phonebook.items():
#     print(name, number)

# users  =  {
#     '+12': 'April',
#     '+25': 'Sam',
#     '+37': 'Martin'
# }
#
# print(f'Словарь users {users}')
#
# users['+25'] = True
#
# print(f'Словарь users после изменений {users}')

# dictOne = {
#     'Name': 'David',
#     'Age': 32,
#     'Course': 'Accounting',
# }
#
# print(f'Словарь до изменений: {dictOne}')
#
# dictOne.pop("Name")
#
# print(f'Словарь после изменений: {dictOne}')

# dictTwo = {
#     'Name': 'David',
#     'Age': 32,
#     'Course': 'Accounting',
# }
#
# print(f'Исходный словарь: {dictTwo}')
#
# print(f'Значение параметра Age: {dictTwo.get("Age")}')