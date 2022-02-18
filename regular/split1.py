import re

p = re.compile(r'[\n;,]+')
with open('for_split.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    reg_name = re.split(p, text)
    print(reg_name)