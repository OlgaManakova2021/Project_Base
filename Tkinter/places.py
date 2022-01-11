from tkinter import *

root = Tk()
root.title("Форма регистрации")
root.geometry('505x680+200+200')

img = PhotoImage(file='icon.png')
l=Label(image=img).place(x=1,y=100)

Button(text="Sign Up",width=15,height=2,bg='#00AA72',fg='white',font='arial 18').place(x=17,y=17)
Button(text="Log In",width=15,height=2,bg='grey',fg='white',font='arial 18').place(x=260,y=17)

Label(text="Sign Up for Free",width=25,fg='#0000aa',font='arial 25').place(x=17,y=150)

Label(text="First Name",width=8,fg='#0000aa',font='arial 8').place(x=17,y=220)
Label(text="Last Name",width=8,fg='#0000aa',font='arial 8').place(x=260,y=220)
Entry(width=10, font='arial 28').place(x=17,y=250)
Label(text="Email Adress",width=12,fg='#0000aa',font='arial 8').place(x=17,y=303)
Entry(width=10, font='arial 28').place(x=260,y=250)
Entry(width=22, font='arial 28').place(x=17,y=330)
Label(text="Set A Password",width=12,fg='#0000aa',font='arial 8').place(x=17,y=385)
Entry(width=22, font='arial 28').place(x=17,y=405)

Button(text="GET STARTED",width=19,height=1,bg='#00AA72',fg='white',font='arial 30').place(x=17,y=500)

root.mainloop()