import os

# вывести текущую директорию
# print("Текущая директория:", os.getcwd())

# создать пустой каталог (папку)
# os.mkdir("folder")

# повторный запуск mkdir с тем же именем вызывает FileExistsError,
# вместо этого запустите:
# if not os.path.isdir("folder"):
#      os.mkdir("folder")

# изменение текущего каталога на 'folder'
# os.chdir("folder")
# Еще раз выведем рабочий каталог:
# вывод текущей папки
# print("Текущая директория изменилась на folder:", os.getcwd())

# вернуться в предыдущую директорию
# os.chdir("..")

# сделать несколько вложенных папок
os.makedirs("nested1/nested2/nested3")
# print("Текущая директория:", os.getcwd())
