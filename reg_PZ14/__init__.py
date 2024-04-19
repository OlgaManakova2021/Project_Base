import re

p = re.compile(r'\w+\-?\w+\s\w\.\w\.')
with open('writer.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    reg_name = p.findall(text)
    print(reg_name)



