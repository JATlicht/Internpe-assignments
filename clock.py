from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("Manvith's clock")

def time():
    stime=strftime("%H:%M:%S %p")
    label.config(text=stime)
    label.after(1000,time)

label=Label(root,font=("ds-digital",100), background="black", foreground="red")
label.pack()
time()
mainloop()