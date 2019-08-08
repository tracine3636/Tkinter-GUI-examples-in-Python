from tkinter import * # opens the tkinter class

root = Tk()  #just means open window

listbox = Listbox(root)

for i in range(1,101):
    listbox.insert(END, "List" + str(i))

listbox.pack()                   

root.mainloop() #this keeps the window open

