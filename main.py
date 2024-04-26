from tkinter import *
from tkinter import ttk
#setup
r = Tk()
r.geometry("600x800")
r.title('Calculator')
#buttons
button1 = Button(r, text='1', width=13, height=6).place(x=150, y=355)
button2 = Button(r, text='2', width=13, height=6).place(x=250, y=355)
button3 = Button(r, text='3', width=13, height=6).place(x=350, y=355)
button4 = Button(r, text='4', width=13, height=6).place(x=150, y=455)
button5 = Button(r, text='5', width=13, height=6).place(x=250, y=455)
button6 = Button(r, text='6', width=13, height=6).place(x=350, y=455)
button7 = Button(r, text='7', width=13, height=6).place(x=150, y=555)
button8 = Button(r, text='8', width=13, height=6).place(x=250, y=555)
button9 = Button(r, text='9', width=13, height=6).place(x=350, y=555)
button0 = Button(r, text='0', width=13, height=6).place(x=250, y=655)
buttonAdd = Button(r, text='+', width=8, height=3).place(x=500, y=355)
buttonSub = Button(r, text='-', width=8, height=3).place(x=500, y=455)
buttonMult = Button(r, text='X', width=8, height=3).place(x=500, y=555)
buttonDiv = Button(r, text='/', width=8, height=3).place(x=500, y=655)
#functions

r.mainloop()