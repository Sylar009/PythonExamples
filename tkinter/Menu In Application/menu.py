from tkinter import *

def openClicked():
    print("Open is CLicked")


def quitApplication():
    quit()


root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="open", command=openClicked)
subMenu.add_separator()
subMenu.add_command(label="quit", command=quitApplication)

subMenu2 = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=subMenu2)
subMenu2.add_command(label="undo")
# subMenu2.add_separator()
subMenu2.add_command(label="redo")

root.mainloop()