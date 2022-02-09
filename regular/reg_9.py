import re

s = "<b>Text1</b>Text2<b>Text3</b>"
p = re.compile(r"<b>.*</b>", re.S)
print(p.findall(s))

# выдаст ['<b>Text1</b>Text2<b>Text3</b>']

p = re.compile(r"<b>.*?</b>", re.S)
print(p.findall(s))

p = re.compile(r"<b>(.*?)</b>", re.S)
print(p.findall(s))


