import re	                        # Подключаем модуль
p = re.compile(r"^[0-9]+$", re.S)
if p.search("245"):
    print("Число")	                # Выведет: Число
else:
    print("He число")

if p.search("Строка245"):
    print("Число")
else:
    print("He число")	            # Выведет: He число

