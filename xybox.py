
import tkinter as tk
Window=None
lists1=[]
lists2=[]
canvas=None
def drawbox(canvas,list2,l1,n):
         
    canvas.create_rectangle((list2[n][0], list2[n][1]), (list2[n][2], list2[n][3]), fill="white")
    if l1:
        canvas.create_line(lists2[n][0], lists2[n][1], lists2[n][2], lists2[n][3], fill="black", width=2)
        canvas.create_line(lists2[n][2], lists2[n][1], lists2[n][0] , lists2[n][3], fill="black", width=2)

def msgbox(msgs:str,color:str):
    global Window
    global lists1
    global lists2
    global canvas
    Window = tk.Toplevel(bg=color)
    canvas = tk.Canvas(Window, width=800, height=600, bg=color)
    canvas.bind("<Key>", handle_key)  # Bind key events
    canvas.bind("<Button-1>", handle_mouse_click)  # Bind left mouse button click
    canvas.pack()
    for n in range(10):
        lists2=lists2+[[10,n*25+10,10+20,n*25+10+20]]
        lists1=lists1+[False]
        drawbox(canvas,lists2,lists1[n],n)
        
        
        

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
    for n in range(len(lists2)):
        if x>lists2[n][0] and y>lists2[n][1] and x<lists2[n][2] and y<lists2[n][3]:
            Window.title(f"Mouse clicked at (index {n})")
            lists1[n]=not(lists1[n])
            drawbox(canvas,lists2,lists1[n],n)
            nn=n
            
    if nn<0:
        Window.title(f"Mouse not clicked in any object")

root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='blue', fg='Black',
                              command=lambda:msgbox("mouse click....",'blue'))

button.pack()
root.mainloop()