# 1. Созадайте класс Image
#
# 2. У каждого экземпляра класса должно быть три собственных атрибута
# - resolution
# - title
# - extension
#
# 3. В классе должен быть метод resize, с помощью которого можно поменять
# разрешение изображения.
#
# 4*. В классе должен быть метод title_upper, с помощью которого можно
# имя файла записать в верхнем регистре.
#
# 5. Создайте несколько экземпляров класса Image и вызовите для каждого
# метод resize

class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, value_extension):
        self.extension = value_extension

    def title_upper(self):
        return self.title.upper()

# img_one = Image("120*120", "bird", "png")
# img_one.resize("jpeg")
# print(img_one.extension)
# print(img_one.title_upper())
#
# img_two = Image("340*140", "cat", "jpeg")
# img_two.resize("gif")
# print(img_two.extension)
