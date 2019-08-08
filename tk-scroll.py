from tkinter import * 

root = Tk()  

frame = Frame(root)

scroll = Scrollbar(frame) 
scroll.pack(side=RIGHT, fill= Y) # this packs in the scroll bar on the right side.

listbox = Listbox(frame, yscrollcommand=scroll.set)


for i in range(1,101):  # this creates a range from 1 to 100.
    listbox.insert(END, "List" + str(i)) # this insert the range into the text box.
listbox.pack(side=LEFT) # this packs in the listbox and aligns text to the left side.  

listbox.pack()    #This packs in the listbox into the frame.               
scroll.config(command=listbox.yview) # this configures the scroll function in the y axis.

frame.pack()
root.geometry("300x300") #this creates a bigger sized frame.
root.mainloop() 

