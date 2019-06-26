from tkinter import *
from tkinter import messagebox


def buttonTapped():
    messagebox._show("Message", "Button Clicked")


root = Tk()

Button(root, text="Click Me", command=buttonTapped).pack()

root.mainloop()
