from tkinter import *

# Setup
root = Tk()

# Create a label - piece of text
theLabel = Label(root, text="This is label!")
theLabel.pack()

# Run the loop that waits for events and
# updates the GUI
root.mainloop()
