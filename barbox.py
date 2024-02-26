
import tkinter as tk
#Window=None
def msgbox(msgs:str,color:str,percents:float,w:int):
    Window = tk.Toplevel(bg=color)
    canvas = tk.Canvas(Window, width=800, height=600, bg=color)
    canvas.pack()
    ww=(800//2)-(w//2)
    canvas.create_text((400, 570),text=msgs,fill="white",font='tkDefaeultFont 12')


    canvas.create_rectangle((ww, 550.00-(500.00//100*percents)), (ww+w, 550), fill='black')


root = tk.Tk()
root.title("msgbox")
w:int=200
percents=100
button = tk.Button(root, text="msgbox", bg='red', fg='Black',
                              command=lambda:msgbox(str(percents)+"%",'red',percents,w))

button.pack()
root.mainloop()