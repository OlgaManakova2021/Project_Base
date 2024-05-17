# a = 15
# print(type(a))
#
# str = "Olga"
# print(type(str))

class Car:
    def move(self):
        print("Машина едет")

    def stop(self):
        print("Машина стоит")

class Car_1:
    pass


BMW = Car()
Opel = Car()

# BMW.move()
# BMW.stop()
#
# Opel.stop()
# Opel.move()


# print(BMW)
# print(Opel)
# print(type(BMW))
# print(isinstance(Opel, Car))
# print(isinstance(BMW, Car_1))
# print(isinstance(Opel, object))
# print(BMW == Opel)
# print(id(BMW), id(Opel))

#Атрибуты my_car
print(dir(BMW))
# print(BMW.__dict__)