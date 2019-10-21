from tkinter import*
import random
import time
import mailpy as m
import database as db

root = Tk()
root.geometry("1280x720+0+0")
root.title("^-^ NewsLetter ^-^")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="^-^ NewsLetter ^-^",fg="steel blue",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)


def qexit():
    root.destroy()

def reset():
    db.res()
def send():
    m.send_mail()
def Ref():
    a = txtname.get("1.0",'end-1c')
    b = txtEmail.get("1.0",'end-1c')
    db.dbin(a,b)

def updatem():
    a = txtname.get("1.0",'end-1c')
    b = txtEmail.get("1.0",'end-1c')
    db.update(b,a)

def unsub():
    a = txtname.get("1.0",'end-1c')
    b = txtEmail.get("1.0",'end-1c')
    db.delete(a,b)

#---------------------------------------------------------------------------------------
name = StringVar()
email = StringVar()

lblname = Label(f1, font=( 'aria' ,16, 'bold' ),text="Name",fg="steel blue",bd=10,anchor='w')
lblname.grid(row=1,column=0)
txtname=Text(root,font=( 'aria' ,16, 'bold' ),fg="steel blue",bd=5, height=1, width=50)
txtname.place(relx=0.35, rely=0.45, anchor='n')


lblEmail = Label(f1, font=( 'aria' ,16, 'bold' ),text="Email",fg="steel blue",bd=10,anchor='w')
lblEmail.grid(row=2,column=0)
txtEmail=Text(root,font=( 'aria' ,16, 'bold' ),fg="steel blue",bd=5, height=1, width=50)
txtEmail.place(relx=0.35, rely=0.52, anchor='n')




#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnsignup=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Sign UP!", bg="powder blue",command=Ref)
btnsignup.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=7, column=3)


btnsendmail=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Send Mail", bg="powder blue",command=send)
btnsendmail.grid(row=7, column=0)

btnupdate=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Update E-Mail", bg="powder blue",command=updatem)
btnupdate.grid(row=7, column=4)

btndel=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Unsubscribe", bg="powder blue",command=unsub)
btndel.grid(row=7, column=5)

root.mainloop()
