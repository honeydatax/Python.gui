
import tkinter as tk
#Window=None
returnvalue:str=""
def selectbox(msgs:str,value,color:str,llist:list):
    global returnvalue
    Window = tk.Toplevel(bg=color)
    text_ = tk.Label(Window,text=msgs,height=1, width=50,bg='red')
    text_.pack(pady=5)   
    ls=tk.Listbox(Window, height=10, width=50,bg='red')
    ls.pack(pady=5)
    i=0
    for n in llist:
        if i==0:
            ls.insert(i,"*--------"+n)
        else:
            ls.insert(i,"O--------"+n)
        i+=1
    bo=tk.Button(Window,text="OK",bg=color,command=lambda:value(ls.curselection(),ls,llist))
    bo.pack()
    
    

def setvarssyes(my:int,ls,llist):
    global returnvalue
    returnvalue=my
    for n in llist:
        ls.delete(0)
    i=0
    ii:int=int(my[0])
    print(ii)
    for n in llist:
        if ii==i:
            ls.insert(i,"*--------"+n)
        else:
            ls.insert(i,"O--------"+n)
        i+=1

root = tk.Tk()
root.title("msgbox")
menuss=["8086","80186","80286","80386","80486","arm"]
button = tk.Button(root, text="msgbox", bg='red', fg='Black',command=lambda:selectbox("hello world....",setvarssyes,'red',menuss))
button
button.pack()
root.mainloop()