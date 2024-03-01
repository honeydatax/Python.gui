import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import *
import subprocess
import shutil
import os
from PIL import Image 
from PIL import ImageTk
import PIL


images=None
ccanvas=None
def msgbox(msgs:str,color:str):
    Window = tk.Toplevel(bg=color)

    
    filename = tk.filedialog.askopenfilename(title="load file")
    
    image = Image.open(filename)
    try:
        im =PIL.ImageTk.PhotoImage(image=image, width=800, height=600)
    except:
        try:
            im =PIL.ImageTk.PhotoBitmap(image=image, width=800, height=600)
        except:
            print("bitmap not suport")
    # obtém as dimensões da imagem
    Width, Height = image.size

    # percorre todos os pixels da imagem e muda a cor azul para vermelho
    canvas = tk.Canvas(Window, width=Width, height=Height, bg=color)
    for x in range(Width):
        for y in range(Height):
            # obtém o valor RGB do pixel atual
            rgb= image.getpixel((x, y))
            b=rgb[0]
            g=rgb[1]
            r=rgb[2]
            
            # verifica se o pixel é azul (R=0, G=0, B=255) e o substitui por vermelho (R=255, G=0, B=0)
            #if r == 0 and g == 0 and b == 255:
            s=hex(r+g*256+b*256*256)
            s=s.replace("0x","000000")
            s1=len(s)
            s2=s1-6
            s="#"+s[s2:s1]
            #print(s)
            canvas.create_rectangle((x, y),(x+1,y+1),outline="", fill=s)
    
    
    canvas.pack()
    
    
class BareboneBuilder:
    def __init__(self, root):
        i:int=0
        self.root = root
        self.root.title("")

        # Janela amarela
        self.root.configure(bg='blue')
        # Botões
        self.run_button = tk.Button(self.root, text="load file", command=self.build_kernel)
        self.run_button.pack(pady=5)
       

    def build_kernel(self):
        msgbox("hello world....",'blue') 
       
        
        
       






if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
