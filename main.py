from tkinter import *
root = Tk()
#setup
class BuildCalc():
    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry("600x800")
        self.parent.title('Calculator')
        self.parent.grid()
        self.CreateFrame()
        self.AddButtons()
    def CreateFrame(self):
        self.Frm = Frame(self.parent)
        self.Frm.grid(row = 0, column = 0)
    #buttons
    def AddButtons(self):
        self.bttn1 = Button(self.Frm, text='1', width=13, height=6)
        self.bttn2 = Button(self.Frm, text='2', width=13, height=6)
        self.bttn3 = Button(self.Frm, text='3', width=13, height=6)
        self.bttn4 = Button(self.Frm, text='4', width=13, height=6)
        self.bttn5 = Button(self.Frm, text='5', width=13, height=6)
        self.bttn6 = Button(self.Frm, text='6', width=13, height=6)
        self.bttn7 = Button(self.Frm, text='7', width=13, height=6)
        self.bttn8 = Button(self.Frm, text='8', width=13, height=6)
        self.bttn9 = Button(self.Frm, text='9', width=13, height=6)
        self.bttn0 = Button(self.Frm, text='0', width=13, height=6)
        self.bttnAdd = Button(self.Frm, text='+', width=8, height=3)
        self.bttnSub = Button(self.Frm, text='-', width=8, height=3)
        self.bttnMult = Button(self.Frm, text='X', width=8, height=3)
        self.bttnDiv = Button(self.Frm, text='/', width=8, height=3)

    #def Pressed1(self):





#run
buildcalc = BuildCalc(root)
root.mainloop()
