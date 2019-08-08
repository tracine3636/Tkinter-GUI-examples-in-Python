from tkinter import * # opens the tkinter class

root = Tk()  #just means open window

s = ttk.Scrollbar( parent, orient=VERTICAL, command=listbox.yview)
listbox.configure(yscrollcommand=s.set)

root.mainloop() #this keeps the window open

