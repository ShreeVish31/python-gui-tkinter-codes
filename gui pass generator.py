from tkinter import *
import random

root = Tk()
root.title("PASSWORD GENERATOR")
root.geometry("400x200")
root.resizable(0,0)
root['background'] = 'blue'

def generate():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    sys = "[]{}()*;/,._-@#!$&"

    all = lower+upper+num+sys
    length = 16
    password = "".join(random.sample(all,length))
    passw.set(password)


passw = StringVar()
btn = Button(root,bd=5,fg="black",bg="lightblue",font=("sans",16,"bold"),width=10,text="Generate",command=generate).place(x=125,y=30)

entry = Entry(root,font=("aria",15,"bold"),textvariable=passw,bd=6,width=25,bg="lightgreen").place(x=60,y=90)
#print(password)


root.mainloop()