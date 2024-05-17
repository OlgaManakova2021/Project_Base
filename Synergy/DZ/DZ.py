from tkinter import *
from tkinter import messagebox

def data_entry():
    # при помощи get получаем данные из поля
    a = tf.get()
    # вывод сообщения
    messagebox.showinfo("Вы ввели ", f'{a}')

window = Tk()
window.title("Сообщение от пользователя")
window.geometry('450x300')

# блок frame
frame = Frame(window,padx=15, pady=15)
# позиционирование виджета в окне
frame.pack(expand=True)

# блок по обавлению надписи
lb = Label(frame, text="Введите Ваше сообщение")
# метод grid (текст будет в третьей строке, первом столбце)
lb.grid(row=3, column=1, pady=5)

# блок для ввода пользовательской информации
tf = Entry(frame,)

# указываем, что поле будет находится справа от верхней надписи
tf.grid(row=3, column=2)

# добавление кнопки
btn = Button(frame, text="Вывести сообщение", command=data_entry)
btn.grid(row=5, column=2)

window.mainloop()



