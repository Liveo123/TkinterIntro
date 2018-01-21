# Fitting Widgets in Layout
import tkinter as tk

root = tk.Tk()

one = tk.Label(root, text="One", bg="red", fg="blue")
one.pack()
two = tk.Label(root, text="Two", bg="blue", fg="white")
# The fill means that it fills the frame in the x directtion
two.pack(fill=tk.X)
# Also need to fill on Y.  Needs to be one side for some unknown reason
three = tk.Label(root, text="Three", bg="cyan", fg="black")
three.pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()