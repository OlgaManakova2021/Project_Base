# Генерация таблицы умножения от 3 до 7
table = [
    [x * y for x in range(3, 8)]
    for y in range(3, 8)]
print(table)

