import tkinter as tk

root = tk.Tk()

def button1Click(event):
    print('Left button clicked')

def button2Click(event):
    print('Right button clicked')

button1 = tk.Button(root, text='Click me')
button1.bind("<Button-1>", button1Click)
button1.bind("<Button-2>", button2Click)
button1.pack()

root.mainloop()