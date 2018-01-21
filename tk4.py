import tkinter as tk
import logging

logging.basicConfig(filename="debug.log", level=logging.DEBUG)

root = tk.Tk()

# Create login labels, entry boxes and button
label1 = tk.Label(root, text="name")
label2 = tk.Label(root, text="password")
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
chkBox = tk.Checkbutton(root, text="Keep me checked in")


button = tk.Button(root, text="OK")

# Add the controls to a grid
# sticky moves the label to the east in the current grid element
label1.grid(row=0, sticky=tk.E)  # N.B. Defaults to column=0
label2.grid(row=1, sticky=tk.E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
# The following will set up the checkbutton to go over 2 columns
chkBox.grid(row=2, columnspan=2)
button.grid(row=3, column=1)


# Set up the button
def buttonClick():
    logging.debug(entry1.get())
    logging.debug(entry2.get())


button.config(command=buttonClick)

root.mainloop()
