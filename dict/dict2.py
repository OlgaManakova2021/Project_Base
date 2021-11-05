#Пример демонстрирует ввод значений в словарь, вывод части словаря и всех элементов словаря

person = {
    'name': {
        'last_name': input('Введи фамилию   '),
        'first_name': input('Введи имя   '),
        'middle_name': input('Введи отчество   ')},
    'addres': [input('Введи город  '), input('Введи улицу и номер дома  ')]
}

print('Вывод фамилии - ', person['name']['last_name'])
print('Вывод города и номера дома - ', person['addres'])
print('Вывод всего словаря - ', person)
