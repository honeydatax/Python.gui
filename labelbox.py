
import tkinter as tk
#Window=None
def msgbox(msgs:str,color:str):
    Window = tk.Toplevel(bg=color)
    canvas = tk.Canvas(Window, width=800, height=600, bg=color)
    canvas.pack()
    canvas.create_text((300, 30),text=msgs,fill="black",font='tkDefaeultFont 24')


root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='red', fg='Black',
                              command=lambda:msgbox("hello world....",'red'))

button.pack()
root.mainloop()