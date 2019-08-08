#Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> window=Tk()
>>> window.geometry("300x300")
''
>>> window.title("Welcome")
label1=Label(window,text="Welcome to Tkinter",
font=("arial",16,"bold")).pack()

window.mainloop()
