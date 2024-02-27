
import tkinter as tk
Window=None
lists1=[]
lists2=[]
canvas=None
def msgbox(msgs:str,color:str):
    global Window
    global lists1
    global lists2
    global canvas
    print(msgs)
    Window = tk.Toplevel(bg=color)
    canvas = tk.Canvas(Window, width=800, height=600, bg=color)
    canvas.bind("<Key>", handle_key)  # Bind key events
    canvas.bind("<Button-1>", handle_mouse_click)  # Bind left mouse button click
    canvas.pack()
    for n in range(10):
        l1=[10,n*30+10,10+80,n*30+10+24,color,str(n)]
        drawlabel(l1,canvas)
        lists2=lists2+[l1]
        
        


def drawlabel(l:list,canvass):
    canvass.create_rectangle((l[0], l[1]), (l[2], l[3]), fill="white")
    m=l[2]-l[0]
    m=l[0]+m//2
    mm=l[3]-l[1]
    mmm=l[1]+(mm//2)
    canvas.create_text(( m,mmm),text=l[5],fill=l[4],font='tkDefaeultFont '+str(mm))
def handle_key(event):
    # Your custom logic for key events
    pass

def handle_mouse_click(event):
    # Your custom logic for mouse click events
    global Window
    global lists1
    global lists2
    global canvas
    x=event.x
    y=event.y
    nn=-1
    color="black"
    for n in range(len(lists2)):
        if x>lists2[n][0] and y>lists2[n][1] and x<lists2[n][2] and y<lists2[n][3]:
            Window.title(f"Mouse clicked at (index {n})")
            l1=[lists2[n][0],lists2[n][1],lists2[n][2],lists2[n][3],color,lists2[n][5]]
            drawlabel(l1,canvas)

            nn=n
            
    if nn<0:
        Window.title(f"Mouse not clicked in any object")

root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='red', fg='Black',
                              command=lambda:msgbox("mouse",'red'))

button.pack()
root.mainloop()