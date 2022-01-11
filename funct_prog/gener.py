# Вариант 1
# def sq_all(numbers):
#     for n in numbers:
#         yield n ** 2

# Вариант 2
def sq_all(numbers):
    # оператор for убирается как самостоятельная конструкция
    yield from [n ** 2 for n in numbers]


numbers = [6, 57, 4, 7, 68, 95]
squares = sq_all(numbers)

for i in squares:
    print(i)

