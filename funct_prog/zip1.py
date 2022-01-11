id = [1, 2, 3, 4]
name = ['Меркурий', 'Венера', 'Земля', 'Марс']

rec = zip(id, name) # объединение для двух списков
print(list(rec))

radius = [2439, 6051, 3678, 3376]
rec1 = zip(id, name, radius) # объединение для трех списков
print(list(rec1))

radius_1 = [2439, 6051, 3678]
rec2 = zip(id, name, radius_1) # объединение для трех списков по длине наименьшего
print(list(rec2))

name_dict_1 = {i: nd for i, nd in zip(id, name)} # создание словаря с использованием dict comprehension
print(name_dict_1)

name_dict_2 = dict(zip(id, name)) # создание словаря с использованием dict comprehension
print(name_dict_2)

# добавим в словарь новые значения

new_id = [5]
new_name = ['Юпитер']
name_dict_2.update(zip(new_id, new_name))
print(name_dict_2)

# zip и выполнение расчетов
diff = [a-b for a, b in zip(radius, radius[1:])]
print(diff)