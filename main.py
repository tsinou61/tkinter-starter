# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Hello"
lbl = Label(window, text="I am now going to mess up this code!")

# Place the label in the window at 0, 0
lbl.grid(column=0, row=0)


window.mainloop()     # Keep the window open
