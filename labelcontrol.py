
import tkinter as tk
from tkinter.font import Font
Window=None
lists1=[]
lists2=[]
lists3=[]
canvas=None
def msgbox(msgs:str,color:str):
    global Window
    global lists1
    global lists2
    global lists3
    global canvas

    Window = tk.Toplevel(bg=color)
    canvas = tk.Canvas(Window, width=800, height=600, bg=color)
    canvas.bind("<Key>", handle_key)  # Bind key events
    canvas.bind("<Button-1>", handle_mouse_click)  # Bind left mouse button click
    canvas.pack()
    for n in range(10):
        l1=[10,n*30+10,10+80,n*30+10+24,str(n)+msgs]
        lists3=lists3+[drawlabel(l1,canvas,"black")]
        lists2=lists2+[l1]
        
        


def drawlabel(l:list,canvass,color):
    canvass.create_rectangle((l[0], l[1]), (l[2], l[3]), fill="white")
    m1=l[2]-l[0]
    m=l[0]+m1//2
    mm=l[3]-l[1]-4
    mmm=l[1]+(mm//2)
    llll=len(l[4])

    l1=llll*mm    
    if l1>m1:
        llll=(m1//mm)
    
    ls=l[4]
    
    font = Font(family="Monospace", size=mm-4, weight="bold")
    ters=canvas.create_text(( m,mmm+2),text=ls,fill=color,font=font)
    kl1=len(ls)
    return ters
def handle_key(event):
    # Your custom logic for key events
    pass

def handle_mouse_click(event):
    # Your custom logic for mouse click events
    global Window
    global lists1
    global lists2
    global lists3
    global canvas
    x=event.x
    y=event.y
    nn=-1
    color="black"
    for n in range(len(lists2)):
        if x>lists2[n][0] and y>lists2[n][1] and x<lists2[n][2] and y<lists2[n][3]:
            Window.title(f"Mouse clicked at (index {n})")
            l1=[lists2[n][0],lists2[n][1],lists2[n][2],lists2[n][3],lists2[n][4]]
            canvas.itemconfig(lists3[n],fill='blue')

            nn=n
            
    if nn<0:
        Window.title(f"Mouse not clicked in any object")

root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='blue', fg='Black',
                              command=lambda:msgbox("..........",'blue'))

button.pack()
root.mainloop()