import os

# создать новый текстовый файл
# text_file = open("text.txt", "w")
# # # запись текста в этот файл
# text_file.write("Это текстовый файл")
# text_file.close()

# переименовать text.txt на renamed-text.txt
# os.rename("text.txt", "renamed-text.txt")

# заменить (переместить) этот файл в другой каталог
# os.replace("renamed-text.txt", "folder/renamed-text.txt")

# распечатать все файлы и папки в текущем каталоге
# print("Все папки и файлы:", os.listdir())

# распечатать все файлы и папки рекурсивно
# for dirpath, dirnames, filenames in os.walk("."):
#     # перебрать каталоги
#     for dirname in dirnames:
#         print("Каталог:", os.path.join(dirpath, dirname))
#     # перебрать файлы
#     for filename in filenames:
#         print("Файл:", os.path.join(dirpath, filename))

# удалить созданный файл
# os.remove("folder/renamed-text.txt")

# удалить папку
# os.rmdir("folder")

# удалить вложенные папки
# os.removedirs("nested1/nested2/nested3")

# вывести некоторые данные о файле
print(os.stat("text.txt"))

# например, получить размер файла
print("Размер файла:", os.stat("text.txt").st_size)



