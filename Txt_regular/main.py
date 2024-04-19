from Utils import Regular_Utils as ru

with open('../Files/9_File_judical.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    text_lines = text.split(" ")  # Разделение строки по " "
    text_lines.pop()  # Удалениие последнего элемента списка
    for line in text_lines:
        title = ru.find_name(line)
        print(title)


