import time
import threading
import tkinter as tk
import time
Window=None
endss=True
counts=0
t1=None
def msgbox(msgs:str,color:str,ontimes):
    global t1
    global endss
    global Window

    Window = tk.Toplevel(bg=color)
    lll = tk.Text(Window, height=1, width=80,bg='red')
    lll.pack()
    bo=tk.Button(Window,text="OK",bg=color,command=lambda:quits())
    bo.pack()
    t1 = threading.Thread(target=ontimer, args=(lll,))
    t1.start()

def quits():
    global t1
    global endss
    global Window
    endss=False
 
    t1.join()
   
    time.sleep(2)
    Window.quit()

def ontimer(lll):
    global counts
    global endss
    print (endss)
    while endss:
        lll.delete(1.0, tk.END)
        lll.insert(tk.END,str(time.ctime(time.time())))
        counts+=1
        time.sleep(1)
    
root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='red', fg='Black',
                              command=lambda:msgbox("hello world....hello world....hello world....hello world....",'red',ontimer))

button.pack()
root.mainloop()