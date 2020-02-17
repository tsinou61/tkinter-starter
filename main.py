# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window
window.title("TrevorApp - Still Better than Safari!")
window.geometry('1500x500')
from tkinter.ttk import Progressbar
bar = Progressbar(window, length=200)
from tkinter import Menu
from tkinter.ttk import *
score = 0
hello = Label(window, text=score, font=("Arial Bold", 50))
hello.grid(column=8, row=8)

motivation = Label(window, text="Start the game!", font=("Arial Bold", 20))
motivation.grid(column=7, row=8)

def addToScore():
  global score
  score += 1
  hello['text'] = score
  bar['value'] = score
  bar.grid(column=8, row=7)
  if score == 10:
      motivation['text'] = "Just starting I see!"
  elif score == 50:
        motivation['text'] = "Halfway there!"
  elif score > 100:
        motivation['text'] = "You are done!"
        hello['text'] = "You did it!"


click = Button(window, text="Click", command=addToScore)
click.grid(column = 4 , row = 4)

combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5)
combo.current(1)
combo.grid(column=0, row=6)

lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

second = Label(window, text="Type your name and press the button!", font=("Times New Roman", 20))
second.grid(column=0, row=1)
def clicked():
    res = "Welcome to TrevorApp " + txt.get()
    lbl.configure(text= res)
txt = Entry(window,width=10)
txt.grid(column=0, row=7)

btn = Button(window, text="Click", command=clicked)
btn.grid(column=0, row=3)

btn2 = Button(window, text ="No, Press Me!", command=clicked)
btn2.grid(column=0, row=4)
txt.focus()

chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=8)

rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
rad1.grid(column=0, row=9)
rad2.grid(column=0, row=10)
rad3.grid(column=0, row=11)

var =IntVar()
var.set(score)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin.grid(column=0, row=12)


menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)





window.mainloop()     # Keep the window open