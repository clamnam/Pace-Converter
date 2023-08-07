import tkinter as tk
from tkinter import ttk
val=0
window = tk.Tk()

num_var=tk.StringVar()
str_var=tk.StringVar()

# 

# defining a function that will
# get the name and password and
# print them on the screen
def submit():

	num=num_var.get()
	num =calculator(num)
	print("The num is : " + str(num))
	
	num_var.set("")
	
	


def calculator(num):
    # (num) 
    return float(num)*1.60934



window.title("Conversion Calculator")


# creating a entry for input
# num using widget Entry
num_entry = tk.Entry(window,textvariable = num_var, font=('calibre',10,'normal'))
checkM_Km =tk.Radiobutton(window,text='m-km',command='sel')
checkKm_M =tk.Radiobutton(window,text='km-m',command='sel')

label = tk.Label( text="Welcome to the conversion calculator", pady=30, padx=100, font=100,)
# entry=tk.Entry(window, textvariable= val, font = ('calibre',10,'normal'))

click_here = tk.Button(window, text="Click to Convert", command=submit, padx = 10, pady = 10)

# root.bind("<Return>", calculate)




label.pack()

checkKm_M.pack()
checkM_Km.pack()
label.pack()
num_entry.pack()
click_here.pack()

window.mainloop() 
