from tkinter import *

def showRadioValue():
    print(radioButtonValue.get())


root = Tk()

radioButtonValue = StringVar()

Label(root, text="What is your favourite weather").pack()
Radiobutton(root, text="Sunny", value="Sunny", variable=radioButtonValue).pack()
Radiobutton(root, text="Rainy", value="Rainy", variable=radioButtonValue).pack()
Radiobutton(root, text="Wet", value="Wet", variable=radioButtonValue).pack()
Radiobutton(root, text="Dry", value="Dry", variable=radioButtonValue).pack()
Radiobutton(root, text="Cloudy", value="Cloudy", variable=radioButtonValue).pack()

Button(root, text="Show radio button value", command=showRadioValue).pack()

root.mainloop()