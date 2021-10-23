# программа калькулятор

Mum1 = int(input('Введи 1 число: '))
Mum2 = int(input('Введи 2 число: '))
calc = input('Введи знак операции:  ')
if calc == '+':
    print(Mum1 + Mum2)
elif calc == '*':
    print(Mum1 * Mum2)
elif calc == '/':
    print(Mum1 / Mum2)
elif calc == '-':
    print(Mum1 - Mum2)