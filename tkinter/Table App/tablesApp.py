from tkinter import *


def showTable():
    table = entry.get()
    two = int(table) * 2
    three = int(table) * 3
    four = int(table) * 4
    five = int(table) * 5
    six = int(table) * 6
    seven = int(table) * 7
    eight = int(table) * 8
    nine = int(table) * 9
    ten = int(table) * 10

    labelText1.set(table + " x " + " 1 = " + table)
    labelText2.set(table + " x " + " 2 = " + str(two))
    labelText3.set(table + " x " + " 3 = " + str(three))
    labelText4.set(table + " x " + " 4 = " + str(four))
    labelText5.set(table + " x " + " 5 = " + str(five))
    labelText6.set(table + " x " + " 6 = " + str(six))
    labelText7.set(table + " x " + " 7 = " + str(seven))
    labelText8.set(table + " x " + " 8 = " + str(eight))
    labelText9.set(table + " x " + " 9 = " + str(nine))
    labelText10.set(table + " x " + " 10 = " + str(ten))


root = Tk()

entry = Entry(root)
entry.pack()

Button(root, text="Show Table", command=showTable).pack()

labelText1 = StringVar()
labelText1.set("=======")
Label(root, textvariable=labelText1, bg="green").pack()

labelText2 = StringVar()
labelText2.set("=======")
Label(root, textvariable=labelText2, bg="yellow").pack()

labelText3 = StringVar()
labelText3.set("=======")
Label(root, textvariable=labelText3, bg="pink").pack()

labelText4 = StringVar()
labelText4.set("=======")
Label(root, textvariable=labelText4, bg="brown").pack()

labelText5 = StringVar()
labelText5.set("=======")
Label(root, textvariable=labelText5, bg="blue").pack()

labelText6 = StringVar()
labelText6.set("=======")
Label(root, textvariable=labelText6, bg="cyan").pack()

labelText7 = StringVar()
labelText7.set("=======")
Label(root, textvariable=labelText7, bg="magenta").pack()

labelText8 = StringVar()
labelText8.set("=======")
Label(root, textvariable=labelText8, bg="grey").pack()

labelText9 = StringVar()
labelText9.set("=======")
Label(root, textvariable=labelText9, bg="red").pack()

labelText10 = StringVar()
labelText10.set("=======")
Label(root, textvariable=labelText10, bg="purple").pack()

root.mainloop()
