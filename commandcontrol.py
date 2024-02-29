
import tkinter as tk
from tkinter.font import Font
Window=None
lists1=[]
lists2=[]
lists3=[]
canvas=None
def drawlabel(l:list,canvass,color,l1,n):
    color="white"
    color2="black"   
    if l1:
        color2="black" 
        color="white"

    
    r1=canvas.create_line(l[0], l[1], l[2], l[1], fill=color, width=2)
    r2=canvas.create_line(l[0], l[1], l[0] , l[3], fill=color, width=2)

    r3=canvas.create_line(l[2], l[1], l[2], l[3], fill=color2, width=2)

    r4=canvas.create_line(l[0], l[3], l[2] , l[3], fill=color2, width=2)

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
    return r1,r2,r3,r4

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
        r1,r2,r3,r4=drawlabel(l1,canvas,"black",False,n)
        lists1=lists1+[False]
        lists3=lists3+[r1]+[r2]+[r3]+[r4]
        lists2=lists2+[l1]
        
        


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
            if lists1[n]:
                lists1[n]=not(lists1[n])
                canvas.itemconfig(lists3[n*4],fill='white')
                canvas.itemconfig(lists3[n*4+1],fill='white')
                canvas.itemconfig(lists3[n*4+2],fill='black')
                canvas.itemconfig(lists3[n*4+3],fill='black')
            else:
                lists1[n]=not(lists1[n])
                canvas.itemconfig(lists3[n*4],fill='black')
                canvas.itemconfig(lists3[n*4+1],fill='black')
                canvas.itemconfig(lists3[n*4+2],fill='white')
                canvas.itemconfig(lists3[n*4+3],fill='white')


            nn=n
            
    if nn<0:
        Window.title(f"Mouse not clicked in any object")

root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='blue', fg='Black',
                              command=lambda:msgbox("..........",'blue'))

button.pack()
root.mainloop()