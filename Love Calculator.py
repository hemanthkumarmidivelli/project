from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox
from tkinter import ttk



def ok(e1111):
    name=e.get()
    lname=e2.get()
    name=str(name)
    lname=str(lname)
    if name=="" or lname=="":
        v="Name can not be empty"
    elif name==lname:
        v="Self love : 100%   <3"
    else:
        v="{} loves {} ".format(name,lname)+str(random.randrange(50,101))+"%     <3"
    ans=messagebox.askokcancel("Love Calculator <3",(v),icon='info')
    if ans==0:
        root.destroy()
def okk():
    name=e.get()
    lname=e2.get()
    name=str(name)
    lname=str(lname)
    if name=="" or lname=="":
        v="Name can not be empty"
    elif name==lname:
        v="Self love : 100%   <3"
    else:
        v="{} loves {} ".format(name,lname)+str(random.randrange(50,101))+"%     <3"
    ans=messagebox.askokcancel("Love Calculator <3",(v),icon='info')
    if ans==0:
        root.destroy()
    
    
root=Tk()
root.title("Love calculator <3 by kittu")
root.geometry("100x500")
root.configure(bg="white")




l=Label(root,text="Love Calculator <3",bg="white",fg="red",font=("ink free",20))
l.grid(column=1,row=1)

l1=Label(root,text="Your name",bg="white",fg="black")
l1.grid(column=1,row=2)

e=Entry(root,width=27)
e.grid(column=1,row=3)

l2=Label(root,text="Your crush name",bg="white",fg="black")
l2.grid(column=1,row=5)

e2=Entry(root,width=27)
e2.grid(column=1,row=6)
e.focus()


b=Button(root,command=okk,text="Calculate",bg="red",height=1,width=20)
b.grid(column=1,row=8)
root.bind('<Return>', ok)
root.mainloop()
l2=Label(root,text="Your crush name",bg="white",fg="black")
l2.grid(column=1,row=5)

e2=Entry(root,width=27)
e2.grid(column=1,row=6)


b=Button(root,command=ok,text="Calculate",bg="red",height=1,width=20)
b.grid(column=1,row=8)
root.bind('<Return>', ok)
root.mainloop()
