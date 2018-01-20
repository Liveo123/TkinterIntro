from tkinter import *
from tkinter import ttk
import logging

# Setup file for debug logging
logging.basicConfig(filename="debug.log", level=logging.DEBUG)

# Create basic Tk window
root = Tk()

# Create a button
button = ttk.Button(root, text='Click me!!!')
button.pack()

# Button event (i.e. run when button clicked)
def callback():
    print("Clicked")
button.config(command=callback)

# Test button state (disable and then enable)
button.state(['disabled'])
logging.debug(button.instate(['disabled']))
button.state(['!disabled'])

# Add image to button
logo = PhotoImage(file='Baby.gif')
button.config(image=logo, compound=LEFT)

# Use a small logo instead of a big one
# sample every 5th pixel across (x) and down (y)
smallLogo = logo.subsample(5,5)

# Run the main loop to wait for events and
# update the UI
root.mainloop()