'''

'''
#------------------------------------
# from tkinter import *

# top = Tk()
# # Code to add widgets will go here
# top.mainloop()
#------------------------------------


#------------------------------------
# from tkinter import *
# from tkinter import messagebox

# top = Tk()

# def greet():
#     messagebox.showinfo("Say Hello","HELLO WORLD")
    
# B1 = Button(top, text="Say Hello", command=greet)
# B1.pack()

# top.mainloop()
#------------------------------------


#------------------------------------
from tkinter import *
from tkinter import messagebox

top = Tk()
def helloCallBack():
    messagebox.showinfo("Hello Python","Hello World")
    
def whatTheDogDoin():
    messagebox.showinfo("Snoop Dogg","Who let The Dog Out?\nOH Yes!, I did.")
    
B = Button(top, text="Hello", command=helloCallBack)
B.pack()
C = Button(top, text="Cucumber", command=helloCallBack)
C.pack( side=LEFT )
D = Button(top,text="Dogg", command=whatTheDogDoin)
D.pack(side=BOTTOM)

top.mainloop()
#------------------------------------
