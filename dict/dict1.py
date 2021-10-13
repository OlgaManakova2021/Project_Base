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
t = 0
student = {}
inf = 'Иванов Иван Иванович ПОКС-29 5 3 5 5 4'
inf = inf.split()
student['Фамилия'] = inf[0]
student['Имя'] = inf[1]
student['Отчество'] = inf[2]
student['Группа'] = inf[3]
student['Оценки'] = []
for i in inf[4:]:
    student['Оценки'].append(int(i))
print(student)


# Добавть в словарь новый элемент elephant = слон, если его еще нет в словаре
# a = {'cat': 'кошка', 'dog': 'собака', 'bird': 'птица', 'mouse': 'мышь'}
# if 'elephant' not in a:
#     a['elephant'] = 'слон'
# print(a)

# a = {'cat': 'кошка', 'dog': 'собака', 'bird': 'птица', 'mouse': 'мышь'}
# a.popitem()
# print(a)
# a.popitem()
# print(a)