# Составить функцию определения количества цифр в
# целом числе

def countInt(k):
    t = 0
    while k > 0:
        k //= 10
        t += 1
    return t


Int_Nuber = input("Введи целое число: ")

# while type(Int_Nuber) != int:  # обработка исключений
#     try:
#         Int_Nuber = int(Int_Nuber)
#     except ValueError:
#         print("Неправильно ввели!")
#         Int_Nuber = input("Введите целое число: ")

print('Количество цифр в цисле:   ', countInt(Int_Nuber))
