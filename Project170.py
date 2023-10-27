from tkinter import *
from math import *

root = Tk()
root.title('Grade Calculator')
root.geometry('500x500')
root.configure(bg = 'snow')

class Report3rd():
    def __init__(self, ela, math):
        self.ela = ela
        self.math = math
    
    def getPercent(self):
        return round((self.ela + self.math) / 2)
    
class Report4th():
    def __init__(self, ela, math, sci):
        self.ela = ela
        self.math = math
        self.sci = sci
    
    def getPercent(self):
        return round((self.ela + self.math + self.sci) / 3)
    
class Report5th():
    def __init__(self, ela, math, sci, hstry):
        self.ela = ela
        self.math = math
        self.sci = sci
        self.hstry = hstry
    
    def getPercent(self):
        return round((self.ela + self.math + self.sci + self.hstry) / 4)

grade1 = Report3rd(84, 96)
grade2 = Report4th(83, 94, 100)
grade3 = Report5th(86, 97, 100, 90)

def show3rd():
    lbl3rd['text'] = f'{ grade1.getPercent() }%'
def show4th():
    lbl4th['text'] = f'{ grade2.getPercent() }%'
def show5th():
    lbl5th['text'] = f'{ grade3.getPercent() }%'

btn3rd = Button(root, text = 'Show 3rd Grades', command = lambda: show3rd())
btn3rd.place(relx = 0.45, rely = 0.4, anchor = E)
btn4th = Button(root, text = 'Show 4th Grades', command = lambda: show4th())
btn4th.place(relx = 0.45, rely = 0.5, anchor = E)
btn5th = Button(root, text = 'Show 5th Grades', command = lambda: show5th())
btn5th.place(relx = 0.45, rely = 0.6, anchor = E)

lbl3rd = Label(root, text = '', bg = 'light blue')
lbl3rd.place(relx = 0.55, rely = 0.4, anchor = W)
lbl4th = Label(root, text = '', bg = 'light blue')
lbl4th.place(relx = 0.55, rely = 0.5, anchor = W)
lbl5th = Label(root, text = '', bg = 'light blue')
lbl5th.place(relx = 0.55, rely = 0.6, anchor = W)

root.mainloop()