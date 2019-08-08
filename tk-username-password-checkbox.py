from tkinter import * # opens the tkinter class

root = Tk()  #just means open window

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

entry_1 = Entry(root) #entry line for user            
entry_2 = Entry(root) #entry line for user
                
label_1.grid(row=0, sticky =E) # sticky aligns your text fields to the east or left. 
label_2.grid(row=1, sticky =E) # sticky aligns your text fields to the east or left.

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)                
                
c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)






root.mainloop() #this keeps the window open

