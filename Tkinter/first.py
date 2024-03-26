from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Привет осень!")
root.geometry('300x40')

def button_clicked():
    print("Hello мир!")

def close():
    root.destroy()
    root.quit()

button = ttk.Button(root,
    text="Press Me",
    command=button_clicked)
button.pack(fill=BOTH)

root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()
