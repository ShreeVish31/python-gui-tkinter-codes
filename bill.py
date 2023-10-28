from tkinter import *

root = Tk()

root.title("BILL MANAGEMENT SYSTEM")
root.geometry("1000x500")
root.resizable(False,False)

def Reset():
    entry_dosa.delete(0,END)
    entry_samosa.delete(0,END)
    entry_vadapav.delete(0,END)
    entry_idli.delete(0,END)
    entry_sandwich.delete(0,END)
    entry_soup.delete(0,END)
    entry_tea.delete(0,END)
    entry_total.delete(0,END)

def Total():
    try:a1=int(dosa.get())
    except:a1=0

    try:a2=int(samosa.get())
    except:a2=0

    try:a3=int(vadapav.get())
    except:a3=0

    try:a4=int(idli.get())
    except:a4=0

    try:a5=int(sandwich.get())
    except:a5=0

    try:a6=int(soup.get())
    except:a6=0

    try:a7=int(tea.get())
    except:a7=0
    

    #pricing
    c1=60*a1
    c2=15*a2
    c3=20*a3
    c4=80*a4
    c5=40*a5
    c6=50*a6
    c7=10*a7

    total_cost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f' %total_cost)
    Total_bill.set(string_bill)



Label(text="BILL MANAGEMENT",font=("Arial",30),bg="black",fg="white",width="300",height="2").pack()

#menu card
f=Frame(root,bg="orange",highlightbackground="black",highlightthickness=1,width=300,height=390)
f.place(x=5,y=100)

Label(f,text="Menu Card",font=("Gabriola",40,"bold"),fg="black",bg="orange").place(x=40,y=0)

Label(f,font=("Lucida Calligraphy",15,"bold"),text="Dosa......Rs.60/plate",fg="black",bg="orange").place(x=15,y=90)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Samosa.....Rs.15/pc",fg="black",bg="orange").place(x=15,y=120)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="VadaPav.....Rs.20/pc",fg="black",bg="orange").place(x=15,y=150)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Idli.....Rs.80/plate",fg="black",bg="orange").place(x=15,y=180)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Sandwich.....Rs.40/pc",fg="black",bg="orange").place(x=15,y=210)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Soup.....Rs.50/bowl",fg="black",bg="orange").place(x=15,y=240)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Tea.....Rs.10/cup",fg="black",bg="orange").place(x=15,y=270)

#bill
f2=Frame(root,bg="skyblue",highlightbackground="black",highlightthickness=1,width=300,height=390)
f2.place(x=690,y=100)

bill=Label(f2,text="Bill",font=("Gabriola",30,"bold"),bg="skyblue")
bill.place(x=120,y=0)

#entry work
f1=Frame(root,bd=5,height=390,width=300,relief=RAISED)
f1.place(x=310,y=100)

dosa=StringVar()
samosa=StringVar()
vadapav=StringVar()
idli=StringVar()
sandwich=StringVar()
soup=StringVar()
tea=StringVar()
Total_bill=StringVar()

#label
l1_dosa=Label(f1,font=("aria",20,"bold"),text="Dosa",width=12,fg="blue4")
l1_samosa=Label(f1,font=("aria",20,"bold"),text="Samosa",width=12,fg="blue4")
l1_vadapav=Label(f1,font=("aria",20,"bold"),text="VadaPav",width=12,fg="blue4")
l1_idli=Label(f1,font=("aria",20,"bold"),text="Idli",width=12,fg="blue4")
l1_sandwich=Label(f1,font=("aria",20,"bold"),text="Sandwich",width=12,fg="blue4")
l1_soup=Label(f1,font=("aria",20,"bold"),text="Soup",width=12,fg="blue4")
l1_tea=Label(f1,font=("aria",20,"bold"),text="Tea",width=12,fg="blue4")
l1_total=Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="lightyellow",bg="black")
l1_total.place(x=10,y=55)

l1_dosa.grid(row=1,column=0)
l1_samosa.grid(row=2,column=0)
l1_vadapav.grid(row=3,column=0)
l1_idli.grid(row=4,column=0)
l1_sandwich.grid(row=5,column=0)
l1_soup.grid(row=6,column=0)
l1_tea.grid(row=7,column=0)


#entry
entry_dosa=Entry(f1,font=("aria",20,"bold"),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_samosa=Entry(f1,font=("aria",20,"bold"),textvariable=samosa,bd=6,width=8,bg="lightpink")
entry_vadapav=Entry(f1,font=("aria",20,"bold"),textvariable=vadapav,bd=6,width=8,bg="lightpink")
entry_idli=Entry(f1,font=("aria",20,"bold"),textvariable=idli,bd=6,width=8,bg="lightpink")
entry_sandwich=Entry(f1,font=("aria",20,"bold"),textvariable=sandwich,bd=6,width=8,bg="lightpink")
entry_soup=Entry(f1,font=("aria",20,"bold"),textvariable=soup,bd=6,width=8,bg="lightpink")
entry_tea=Entry(f1,font=("aria",20,"bold"),textvariable=tea,bd=6,width=8,bg="lightpink")
entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
entry_total.place(x=30,y=100)

entry_dosa.grid(row=1,column=1)
entry_samosa.grid(row=2,column=1)
entry_vadapav.grid(row=3,column=1)
entry_idli.grid(row=4,column=1)
entry_sandwich.grid(row=5,column=1)
entry_soup.grid(row=6,column=1)
entry_tea.grid(row=7,column=1)

#button
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("sans",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("sans",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()