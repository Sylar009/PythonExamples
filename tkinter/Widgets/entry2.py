from tkinter import *


def showOnLabel():
    labelText.set(entry.get())


root = Tk()

entry = Entry(root, bg="red", fg="yellow")
entry.pack()

# button to clear the text of entry
Button(root, text="show text on Label", command=showOnLabel).pack()

labelText = StringVar()
labelText.set("======")

label = Label(root, textvariable=labelText)
label.pack()

root.mainloop()
