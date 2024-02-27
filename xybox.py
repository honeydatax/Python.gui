
import tkinter as tk
Window=None

def msgbox(msgs:str,color:str):
    global Window
    Window = tk.Toplevel(bg=color)
    canvas = tk.Canvas(Window, width=800, height=600, bg=color)
    canvas.bind("<Key>", handle_key)  # Bind key events
    canvas.bind("<Button-1>", handle_mouse_click)  # Bind left mouse button click
    canvas.pack()
    canvas.create_text((300, 30),text=msgs,fill="black",font='tkDefaeultFont 24')
    
def handle_key(event):
    # Your custom logic for key events
    pass

def handle_mouse_click(event):
    # Your custom logic for mouse click events
    Window.title(f"Mouse clicked at (x={event.x}, y={event.y})")

root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='red', fg='Black',
                              command=lambda:msgbox("mouse click....",'red'))

button.pack()
root.mainloop()