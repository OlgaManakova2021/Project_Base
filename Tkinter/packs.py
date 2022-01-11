from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Кнопки")
root.geometry('600x200+200+200')

button1 = ttk.Button()
button1["text"] = "Это кнопка 1"
button1.pack(side=LEFT)

button2 = Button(text="Это кнопка 2",width=25,height=5,bg='black',fg='red',font='arial 14').pack(side='left')

button3 = Button(text="Это кнопка 3",bg="red",fg="#0000aa").pack(side='left', fill=Y)

root.mainloop()
