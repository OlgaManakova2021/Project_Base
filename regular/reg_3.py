import re
p = re.compile(r"^.+$")	                  # Точка не соответствует \n
print(p.findall("str1\nstr2\nstr3"))      # Ничего не найдено []

p = re.compile(r"^.+$", re.S)             # Теперь точка соответствует \n
print(p.findall("str1\nstr2\nstr3"))      # Строка полностью соответствует ['str1\nstr2\nstr3']

p = re.compile(r"^.+$", re.M)             # Многострочный режим
print(p.findall("str1\nstr2\nstr3"))      # Получили каждую подстроку ['str1', 'str2', 'str3']
