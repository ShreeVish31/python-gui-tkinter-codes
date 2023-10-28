from tkinter import *

root = Tk()
root.title("Mind reader")
root.geometry("300x150")
root.resizable(0,0)

def Click():
    a = Tk()
    a.title("Mind reader output")
    a.geometry("300x150")
    a.resizable(0,0)
    
    a1 = int(read.get())
    l2 = Label(a,text="You are thinking of number "+str(a1)).pack()



read = StringVar()

l1 = Label(root,text="Think of a number between 1 to 10 :").place(x=50,y=10)
e1 = Entry(root,textvariable=read).place(x=80,y=40)
b1 = Button(root,text="Read my mind",command=Click).place(x=100,y=70)


root.mainloop()