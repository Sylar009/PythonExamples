from tkinter import *
from tkinter import ttk

root = Tk()

Button(root, text="tkinter Button").pack()
ttk.Button(root, text="ttk Button").pack()

root.mainloop()