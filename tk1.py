from tkinter import *
from tkinter import ttk
import logging

logging.basicConfig(filename="debug.log", level=logging.DEBUG)

root = Tk()
button = ttk.Button(root, text='Click me!!!')
button.pack()

def callback():
    print("Clicked")

button.config(command=callback)
button.state(['disabled'])
logging.debug(button.instate(['disabled']))
button.state(['!disabled'])
logo = PhotoImage(file='Baby.gif')
button.config(image=logo, compound=LEFT)
root.mainloop()