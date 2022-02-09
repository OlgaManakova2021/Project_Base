import re

p = re.compile(r'^[а-яё]+$', re.I | re.U)
print('Найдено' if p.search('абвгд') else 'Нет')

p = re.compile(r'^[а-яё]+$', re.U)
print('Найдено' if p.search('АБВГДЕЁ') else 'Нет')