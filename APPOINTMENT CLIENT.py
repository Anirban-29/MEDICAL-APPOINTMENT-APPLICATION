import tkinter as tk
from tkinter import *
import socket
from tkinter import messagebox
root=tk.Tk()
root.title("APPOINTMENT")
root.geometry("300x400")
root.config(bg="#189AB4")
root.resizable(False,False)
Label(root,text="REGISTRATION",font=("montserrat",16,'bold'),bg="#f4f5f6").place(x=70,y=20)
def sent():
    id=sid.get()
    nam=name.get()
    dat=date.get()
    d=click.get()
    data=nam+" "+dat+" "+d
    FORMAT='utf-8'

    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ADDR=(id,22222)
    sock.sendto(str.encode(data,FORMAT),ADDR)
    rec,addr=sock.recvfrom(1024)
    rec=rec.decode()
    if rec!="1":
        messagebox.showinfo("Info","SUCCESSFULLY REGISTERED")
    else:
        messagebox.showerror("Error","ERROR ALREADY REGISTERED")
    sock.close()
Label(root,text="SERVER ID",font=("monserrat",12,'bold'),bg="#3AA8C1").place(x=30,y=230)
sid=Entry(root,width=25,fg='Black',bg='White',font=('Arial',10))
sid.place(x=30,y=258) 
Label(root,text="NAME OF THE PATIENT",bg="#add8e6",font=("monserrat",13,"bold")).place(x=30,y=60)
name=Entry(root,width=25,fg="BLACK",bg="WHITE",font=("monserrat",13,"bold"))
name.place(x=30,y=88)
Label(root,text="DATE",bg="#add8e6",font=("monserrat",13,"bold")).place(x=30,y=118)
date=Entry(root,width=18,fg="BLACK",bg="WHITE",font=("ARIAL",13))
date.place(x=30,y=144)
click=StringVar()
click.set("SELECT")
drop=OptionMenu(root,click,"11am-1pm","2pm-5pm","6pm-9pm").place(x=30,y=180)
print(drop)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(),22222))
host=sock.getsockname()
sock.close()
Label(root,text=f'ID: {host}',bg="#f4f5f4").place(x=90,y=360)
d=Button(root,text="REGISTER",font=9,bg="WHITE",command=sent)
d.place(x=30,y=320)
root.mainloop()