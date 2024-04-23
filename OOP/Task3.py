# Создать класс Person с одним атрибутом класса (count), с конструктором __init__ и
# одним статическим методом.
# Увеличение количества созданных экземпляров обеспечить в конструкторе __init__
# Статический метод total_people должен обеспечивать построение и вывод фразы
# о количестве созданных экземпляров

class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @staticmethod
    def total_people():
        return f"Вы создали {Person.count} персон(ы)."

# person1 = Person("John")
# person2 = Person("Jane")
# person3 = Person("Jack")
#
# print(Person.total_people())