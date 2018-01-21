import tkinter as tk
import logging

logging.basicConfig(filename="debug.log", level=logging.DEBUG)


def doNothing():
    logging.debug('doing nothing')

root = tk.Tk()

# Create a menu
menu = tk.Menu(root)

# Create a submenu of myMenu
submenu = tk.Menu(menu)
submenu.add_command(label="New Project...", command=doNothing)
submenu.add_command(label="New...", command=doNothing)
submenu.add_separator()
submenu.add_command(label="Exit", command=doNothing)
menu.add_cascade(label="File", menu=submenu)

# Create another submenu
editMenu = tk.Menu(menu)
editMenu.add_command(label="Redo", command=doNothing)
menu.add_cascade(label="edit", menu=editMenu)

# Add the menu to root
root.config(menu=menu)
simpleApp.py
root.mainloop()
