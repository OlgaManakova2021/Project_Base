from tkinter import *

root = Tk()
root.title("Анкета участника")
root.geometry('300x100+200+200')

Label(text="Имя").grid(row=0, column=0, sticky=E)
Label(text="Фамилия").grid(row=1, column=0, sticky=E)

Entry().grid(row=0, column=1)
Entry().grid(row=1, column=1)

Checkbutton(text="Согласен с обработкой персональных данных").grid(columnspan=2)

root.mainloop()