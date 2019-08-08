from tkinter import * 

root = Tk()  

def printName(event): # an event is something the user can do.i.e something on keyboard or mouse.
    print("hello my name is Tim")

button1 = Button(root, text="Print my name") 
button1.bind("<button>", printName) #the bind function takes two parameters 1. What event are you waiting for to occur. 2.What function do you want to use when that event occurs.
button1.pack()


root.mainloop() 

