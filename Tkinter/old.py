from tkinter import *
root=Tk()
def leftclick(event):
    print('Вы нажали левую кнопку мыши')
def rightclick(event):
    print('Вы нажали правую кнопку мыши')

button1 = Button(root,text=u'Нажми')
button1.pack()
button1.bind('<Button-1>', leftclick)
button1.bind('<Button-3>', rightclick)
root.mainloop()