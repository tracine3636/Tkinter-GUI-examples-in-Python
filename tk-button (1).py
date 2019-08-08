from tkinter import *

root = Tk()  #) just means open window

topFrame = Frame(root) #top frame pack in
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red") #fg color
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack() #This will pack in the buttons to make them display
button2.pack()
button3.pack()
button4.pack()





root.mainloop() #this keeps the window open

