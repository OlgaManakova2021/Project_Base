# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def prn(self, name, age):
#         print(self.name, self.age)
#
# dog1 = Dog("Rex", 3)
# #dog1.prn

# class Company:
#     department = 15
#
#     def __init__(self, surname, age, department = 15):
#         self.surname = surname
#         self.age = age
#         self.department = department
#
# s1 = Company("Иванов", 23, 14)
# s2 = Company("Сидоров", 24, 16)
# s3 = Company("Петров", 30, 4)

class School:
    def __init__(self, id, age, population):
        self.id = id
        self.age = age
        self.population = population

one = School(13, 25,1500)

print("Паметр id:  ", one.id)
print("Параметр age (начальное значение):  ", one.age)
print("Параметр population (начальное значение):  ", one.population)

one.age = 27
one.population = 1650

print("Параметр age (финальное значение):  ", one.age)
print("Параметр population (финальное значение):  ", one.population)


