import tkinter as tk
import logging

logging.basicConfig(filename="debug.log", level=logging.DEBUG)

root = tk.Tk()

# Create login labels, entry boxes and button
label1 = tk.Label(root, text="name")
label2 = tk.Label(root, text="password")
entry1 = tk.Entry(root, bg="green")
entry2 = tk.Entry(root)
button = tk.Button(root, text="OK")

# Add the controls to a grid
label1.grid(row=0)  # N.B. Defaults to column=0
label2.grid(row=1)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
button.grid(row=2, column=1)


# Set up the button
def buttonClick():
    logging.debug(entry1.get())
    logging.debug(entry2.get())


button.config(command=buttonClick)

root.mainloop()
