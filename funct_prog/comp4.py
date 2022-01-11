# выбрать все гласные буквы из исходной фразы
fraza = "я изучаю язык Питон"
new_fraza = {i for i in fraza if i in 'аеёиоуэюя'}
print(new_fraza)

#в словаре в качестве значения ключа поместить его квадрат
squares = {i: i * i for i in range(10)}
print(squares)
