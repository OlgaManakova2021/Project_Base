from tkinter import *
from tkinter import messagebox

# умножение
def calculate_mult():
    # при помощи get получаем данные из первого поля
    a = int(tf.get())
    # при помощи get получаем данные из второго поля
    b = int(tf_2.get())
    # умножение чисел
    res = a * b

    # вывод результата
    messagebox.showinfo("Результаты вычисления", f'Результат = {res}')

# деление
def calculate_div():
    # при помощи get получаем данные из первого поля
    a = int(tf.get())
    # при помощи get получаем данные из второго поля
    b = int(tf_2.get())
    # деление чисел
    res = a / b

    # вывод результата
    messagebox.showinfo("Результаты вычисления", f'Результат = {res}')

# сложение
def calculate_add():
    # при помощи get получаем данные из первого поля
    a = int(tf.get())
    # при помощи get получаем данные из второго поля
    b = int(tf_2.get())
    # сложение чисел
    res = a + b

    # вывод результата
    messagebox.showinfo("Результаты вычисления", f'Результат = {res}')
#
# вычитание
def calculate_sub():
    # при помощи get получаем данные из первого поля
    a = int(tf.get())
    # при помощи get получаем данные из второго поля
    b = int(tf_2.get())
    # вычитание чисел
    res = a - b
    # вывод результата
    messagebox.showinfo("Результаты вычисления", f'Результат = {res}')

window = Tk()
window.title("Калькулятор умножения чисел")
window.geometry('450x300')

# блок frame
frame = Frame(window,padx=25, pady=25)
# позиционирование виджета в окне
frame.pack(expand=True)

# блок по обавлению надписи
lb = Label(frame, text="Введите первое число")
# метод grid (текст будет в третьей строке, первом столбце)
lb.grid(row=3, column=1, pady=5)

lb_2 = Label(frame, text="Введите второе число")
# етод grid (текст будет в четвертой строке, первом столбце)
lb_2.grid(row=4, column=1, pady=5)

# блок для ввода пользовательской информации
tf = Entry(frame,)
# указываем, что поле будет находится справа от верхней надписи
tf.grid(row=3, column=2)

# добавление второго поля для ввода информации
tf_2 = Entry(frame,)
tf_2.grid(row=4, column=2)

# добавление кнопки "Умножение"
btn = Button(frame, text="Умножение", command=calculate_mult)
btn.grid(row=5, column=2)

# добавление кнопки "Деление"
btn_2 = Button(frame, text="Деление", command=calculate_div)
btn_2.grid(row=5, column=1)

# добавление кнопки "Вычитание"
btn_3 = Button(frame, text="Вычитание", command=calculate_sub)
btn_3.grid(row=6, column=1)

# добавление кнопки "Сложение"
btn_4 = Button(frame, text="Сложение", command=calculate_add)
btn_4.grid(row=6, column=2)

window.mainloop()