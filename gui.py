import tkinter as tk
from tkinter import ttk



def calculator(num):
    return num*1.60934

window = tk.Tk()
window.title("Conversion Calculator")
label = tk.Label( text="Welcome to the conversion calculator", pady=30, padx=100, font=100,)
click_here = tk.Button(window, text="Click to Convert", command=calculator, padx = 10, pady = 10)
w = tk.Entry(window)
# root.bind("<Return>", calculate)




label.pack()
w.pack()
click_here.pack()

window.mainloop() 
