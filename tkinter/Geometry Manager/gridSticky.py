from tkinter import *
from tkinter import ttk

root = Tk()

label1 = Label(root, text="Label 1", bg="red")
label1.grid(row=0, column=0, ipadx=50, ipady=50)

label2 = Label(root, text="Label 2", bg="green")
label2.grid(row=0, column=1, sticky=W+E)

label3 = Label(root, text="Label 3", bg="pink")
label3.grid(row=1, column=0, sticky=W)

label4 = Label(root, text="Label 4", bg="blue")
label4.grid(row=1, column=1, ipadx=50, ipady=50)

root.mainloop()