# В заданной строке найти все прописные буквы, посчитать их количество.
# Использовать библиотеку string

from string import ascii_uppercase

string_new = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
str_1 = [i for i in string_new if i in ascii_uppercase]
print(len(str_1))
print(str_1)


