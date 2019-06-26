from tkinter import *

root = Tk()

Label(root, text="Which one is your favourite?").pack()

Checkbutton(root, text="Milk").pack()

Checkbutton(root, text="Apple Juice").pack()

Checkbutton(root, text="Mango Juice").pack()

root.mainloop()