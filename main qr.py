from tkinter import *
import pyqrcode
from pyqrcode import QRCode
#from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title("QR CODE")
root.geometry("800x500")
root.resizable(0,0)
root['background'] = 'red'


def click():
    
    text = link.get()
    url=pyqrcode.create(text)
    url.png("user.png", scale=7)

    messagebox.showinfo("QR SAVED","QR CODE IS SAVED...!!\nCLICK 'SHOW QR' TO VIEW QR")
    

def show():
    '''sh = Tk()
    sh.geometry("400x400")
    sh.resizable(0,0)'''
    lb1 = Label(root,text="SCAN THIS",font="arial 20",bg='red').place(x=500,y=20)
    global im
    im = PhotoImage(file = 'D:/Projects/websites/hfd/qr code/user.png')
    #lbb = ttk.Label(root, image= im,width=30).place(x=140,y=160)
    view.config(image=im)
    
view = Label(root,bg='red')
view.pack(padx=50,pady=50,side=RIGHT)

lb = Label(root,text="CONVERT ANY URL OR LINK\nINTO QR CODE AT ONE CLICK",font="arial 15",bg='red').place(x=50,y=10)

link = StringVar()

en = Entry(root, width=28, font="arial 15",textvariable=link).place(x=45,y=70)

btn = Button(root, text="GENERATE",width=10,height=1, bg="black", fg="white",font="arial 12",command=click).place(x=140,y=110)

btn1 = Button(root, text="SHOW QR",width=10,height=1, bg="black", fg="white",font="arial 12",command=show).place(x=140,y=160)


root.mainloop()
