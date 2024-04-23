class Note:
    def __init__(self, text):
        self.text = text
        self.count = 0

    def upcount(self):
        self.count += 1

note1 = Note("Задача 1")
# print(note1.__dict__)
# print(dir(note1))
# print(note1.text)
#
# note1.upcount()
# print(note1.count)
# note1.upcount()
# print(note1.count)

# Привязанные методы
print(note1.upcount) # bound - метод является привязанным для экземпляра note1
print(Note.upcount) # function -  с точки зрения класса Note upcount является обычной функцией
