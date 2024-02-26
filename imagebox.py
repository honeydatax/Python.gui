import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def msgbox(msgs:str,color:str):
    filename = filedialog.askopenfilename(title="load file")
    
    img = plt.imread(filename)
    #plt.scatter(x,y,zorder=1)
    plt.imshow(img, zorder=0, extent=[0.5, 8.0, 1.0, 7.0])
    plt.show()


root = tk.Tk()
root.title("msgbox")
button = tk.Button(root, text="msgbox", bg='red', fg='Black',
                              command=lambda:msgbox("hello world....",'red'))

button.pack()
root.mainloop()
