import tkinter as tk
from tkinter import *
import socket
from tkinter import messagebox
root=tk.Tk()
root.title("SERVER DATABASE")
root.geometry("300x300")
root.config(bg="#189AB4")
root.resizable(False,False)
Label(root,text="TODAYS APPOINTMENTS",font=("montserrat",16,'bold'),bg="#f4f5f6").place(x=20,y=5)
def update():
    messagebox.showinfo("Info","SUCCESSFULLY STARTED THE SERVER")
    FORMAT='utf-8'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((socket.gethostname(), 22222))
    client,addr = sock.recvfrom(1024)
    f=open("a.txt","r")
    readfile=f.readlines()
    f.close()
    client=client.decode()
    print(client)
    y=client.split()
    flag="0"
    for line in readfile:
        if line.find(y[0])!=-1:
            s=line.split()
            if(s[1]==y[1]):
                flag="1"
                sock.sendto(flag.encode(FORMAT),addr)
    if flag!="1":
        sock.sendto(flag.encode(FORMAT),addr)
        f=open("a.txt","a")
        for i in range(len(y)):
            f.write(y[i]+" ")
        f.write("\n")
        f.close()
def show():
    m=open("a.txt","r")
    con=m.read()
    tb=tk.Text(root,height=10,width=35)
    tb.insert(1.0, "{}".format(con))
    tb.place(x=9,y=40)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((socket.gethostname(),22222))
host=sock.getsockname()
sock.close()
Label(root,text=f'ID: {host}',bg="#f4f5f4").place(x=90,y=280)
d=Button(root,text="START",font=9,bg="WHITE",command=update)
d1=Button(root,text="SHOW",font=9,bg="WHITE",command=show)
d.place(x=30,y=220)
d1.place(x=230,y=220)
root.mainloop()