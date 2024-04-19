# Задание 1
# Изменить конструктор класса, добавив атрибут iscompleted (True/False).
# Создать экземпляр с новым атрибутом, вывести все значения собственных
# атрибутов экземпляра (__dict__).
# Обеспечить увеличение count на величину, передаваемую в качестве аргумента
# Создать новую функцию reset_count, которая будет обнулять счетчик выполненных задач
# Проверить содержимое магической переменной __dict__

class NoteTwo:
    def __init__(self, text, iscompleted=False):
        self.text = text
        self.count = 0
        self.iscompleted = iscompleted

    def upcount(self, value):
        self.count += value

    def reset_count(self):
        self.count = 0

# note1_two = NoteTwo("Задача 2", True)
# print(note1_two.iscompleted)
# print(note1_two.__dict__)
# note1_two.upcount(4)
# print(note1_two.count)
# note1_two.reset_count()
# print(note1_two.count)
