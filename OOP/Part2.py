class Posts:
    def __init__(self, text):
        self.text = text
        self.count = 2

    def upcount(self):
        self.count += 2

post1 = Posts("Пост 1")
# print(post1.__dict__)
# print(dir(post1))

post2 = Posts("Пост 2")
# print(post2.__dict__)
# print(dir(post2))

print(post1.text)

print(post1.count)
post1.upcount()
print(post1.count)
post1.upcount()
print(post1.count)

print(post2.text)
print(post2.count)
post2.upcount()
print(post2.count)
post2.upcount()
print(post2.count)



# Привязанные методы
# print(note1.upcount) # bound - метод является привязанным для экземпляра note1
# print(Note.upcount) # function -  с точки зрения класса Note upcount является обычной функцией
