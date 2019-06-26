from tkinter import *

def clearText():
    entry.delete(0,END)

root = Tk()

entry = Entry(root, bg="red", fg="yellow")
entry.pack()

# button to clear the text of entry
Button(root, text="Clear Text Box", command=clearText).pack()

root.mainloop()