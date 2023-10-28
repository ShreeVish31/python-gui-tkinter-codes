from tkinter import *

top = Tk()
top.geometry("200x80")
mb = Menubutton(top, text="Menubutton")
mb.grid()

mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton(label='Contact', variable=cVar)
mb.menu.add_checkbutton(label='About', variable=aVar)

mb.pack()

top.mainloop()
