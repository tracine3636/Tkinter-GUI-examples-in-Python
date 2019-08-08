from tkinter import * # opens the tkinter class

root = Tk()  #) just means open window

def printName():
    print("hello my name is Tim")

button_1 = Button(root, text="Print my name", command=printName)
button_1.pack()


root.mainloop() #this keeps the window open

