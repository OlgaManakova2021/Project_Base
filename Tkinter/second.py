#Даны три целых числа. Найти количество положительных и
# количество отрицательных чисел в исходном наборе.

from tkinter import *

def count_num(event):
    t = 0
    r: int = 0

    n1 = int(num1.get())
    n2 = int(num2.get())
    n3 = int(num3.get())

    t = t + 1 if n1 > 0 and n1 != 0 else t
    t = t + 1 if n2 > 0 and n2 != 0 else t
    t = t + 1 if n3 > 0 and n3 != 0 else t

    r = r + 1 if n1 < 0 and n1 != 0 else r
    r = r + 1 if n2 < 0 and n2 != 0 else r
    r = r + 1 if n3 < 0 and n3 != 0 else r

    positive['text'] = "Положительных", t
    negative['text'] = "Отрицательных", r

root = Tk()
root.title("Поиск положительных и отрицательных чисел")
root.geometry("300x200+200+200")


Label(text="Первое число").grid(row=1, column=0)
num1 = Entry()
num1.grid(row=1, column=1)


Label(text="Второе число").grid(row=2, column=0)
num2 = Entry()
num2.grid(row=2, column=1)

Label(text="Третье число").grid(row=3, column=0)
num3 = Entry()
num3.grid(row=3, column=1)

button1 = Button(text="Обработать")
button1.grid(row=4, column=1)

positive = Label()
positive.grid(row=5, column=1)

negative = Label()
negative.grid(row=6, column=1)


button1.bind('<Button-1>',count_num)


root.mainloop()



