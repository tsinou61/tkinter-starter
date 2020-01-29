# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window
window.title("TrevorApp - Still Better than Safari!")
window.geometry('1500x500')
from tkinter.ttk import *
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1)
combo.grid(column=0, row=3)
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
second = Label(window, text="Type your name and press the button!", font=("Times New Roman", 20))
second.grid(column=0, row=1)
def clicked():
    res = "Welcome to TrevorApp " + txt.get()
    lbl.configure(text= res)
txt = Entry(window,width=10)
txt.grid(column=3, row=0)
btn = Button(window, text="Click", command=clicked)
btn.grid(column=2, row=0)
txt.focus()




window.mainloop()     # Keep the window open
