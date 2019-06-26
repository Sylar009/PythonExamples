from tkinter import *


def onButtonClick():
    labelText.set("Text changed on button clicked")


root = Tk()

labelText = StringVar()
labelText.set("Label")

label = Label(root, textvariable=labelText)
label.pack()

Button(root, text="Click Me", command=onButtonClick).pack()

root.mainloop()
