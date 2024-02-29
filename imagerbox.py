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
    im =PIL.ImageTk.PhotoImage(image=image, width=800, height=600)
    # obtém as dimensões da imagem
    width, height = image.size

    # percorre todos os pixels da imagem e muda a cor azul para vermelho
    """
    for x in range(width):
        for y in range(height):
            # obtém o valor RGB do pixel atual
            #r, g, b = image.getpixel((x, y))
        
            # verifica se o pixel é azul (R=0, G=0, B=255) e o substitui por vermelho (R=255, G=0, B=0)
            #if r == 0 and g == 0 and b == 255:
            #image.putpixel((x, y), (r, g, 255))
    """
    canvas = tk.Canvas(Window, width=800, height=600, bg=color)
    canvas.pack()
    canvas.create_image(0,0,image=im).pack()
    
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
