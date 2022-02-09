import re

p = re.compile(r"[0-9]+")
print("Найдено" if p.match("str123") else "Нет")
# выдаст Нет

print("Найдено" if p.match("str123", 3) else "Нет")
# выдаст Найдено

print("Найдено" if p.match("123str") else "Нет")
# выдаст Найдено

p = r"[0-9]+"
print("Найдено" if re.match(p, "str123") else "Нет")
# выдаст Нет

p = re.compile(r"[0-9]+")
print("Найдено" if p.search("strl23") else "Нет")
# выдаст Найдено

print("Найдено" if p.search("123str") else "Нет")
# выдаст Найдено

print("Найдено" if p.search("123str", 3) else "Нет")
# выдаст Нет

p = r"[0-9]+"
print("Найдено" if re.search(p, "str123") else "Нет")
# выдаст Найдено

p = re.compile("[Pp]ython")
print("Найдено" if p.fullmatch("Python") else "Нет")
# выдаст Найдено

print("Найдено" if p.fullmatch("py") else "Нет")
# выдаст Нет

print("Найдено" if p.fullmatch("PythonWare") else "Нет")
# выдаст Нет

print("Найдено" if p.fullmatch("PythonWare", 0, 6) else "Нет")
# выдаст Найдено
