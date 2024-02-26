from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import font as tkFont
import subprocess
import shutil
import os
import tkinter as tk
#Window=None
returnvalue:str=""
def selectbox(msgs:str,value,color:str):
    #cut you dir or ls list size above 
    lens="24/02/2024  15:57                89"
    lenss=len(lens)
    global returnvalue
    Window = tk.Toplevel(bg=color)
    text_ = tk.Label(Window,text=msgs,height=1, width=50,bg='red')
    result = subprocess.check_output("dir *.*", stderr=subprocess.STDOUT, shell=True, text=True)
    result=result.replace("\r","\n")
    result=result.replace("\n\n","\n")
    llist=result.split("\n")
    text_.pack(pady=5)   
    ls=tk.Listbox(Window, height=10, width=50,bg='red')
    ls.pack(pady=5)
    i=0
    for n in llist:
        nn=n.find("\\")

        nnn=n.find("byte")
        n=n[lenss:]
        if n.strip()!="" and nn<0 and nnn<0:
            if i==0:
                ls.insert(i,"X--------"+n)
            else:
                ls.insert(i,"---------"+n)
            i+=1
    bo=tk.Button(Window,text="OK",bg=color,command=lambda:value(ls.curselection(),ls,llist,lenss))
    bo.pack()
    
    

def setvarssyes(my:int,ls,llist,lenss):
    global returnvalue
    returnvalue=my
    for n in llist:
        ls.delete(0)
    i=0
    ii:int=int(my[0])
    
    for n in llist:
        nn=n.find("\\")
        nnn=n.find("byte")
        n=n[lenss:]
        if n.strip()!="" and nn<0 and nnn<0:

            if ii==i:
                ls.insert(i,"X--------"+n)
            else:
                ls.insert(i,"---------"+n)
            i+=1

root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='red', fg='Black',command=lambda:selectbox("select a file",setvarssyes,'red'))
button
button.pack()
root.mainloop()