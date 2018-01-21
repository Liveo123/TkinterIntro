import tkinter as tk
import tkinter.messagebox
import logging

logging.basicConfig(filename="debug.log", level=logging.DEBUG)


def doNothing():
    logging.debug('doing nothing')

def showMessage():
    tk.messagebox.showinfo('This is the title', 'Monkeys can live 300 years.')

def askQuestion():
    answer = tk.messagebox.askquestion('Q1', 'Are you funky?')
    if answer == 'yes':
        logging.debug("Yes pressed")
    else:
        logging.debug("No pressed")

root = tk.Tk()

# ****************  Create a menu  *****************

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


# ****************  Create a toolbar  *****************
toolbar = tk.Frame(root)

# Create and add the buttons

# First is a text button
insertButton = tk.Button(toolbar, text='Insert Image', command=askQuestion)
insertButton.pack(side=tk.LEFT, padx=2, pady=2)

# Second is an image button
babyButton = tk.Button(toolbar, command=showMessage)
babyImg = tk.PhotoImage(file='BabyIcon.gif')
babyButton.config(image=babyImg, compound=tk.RIGHT)
babyButton.pack(side=tk.LEFT, padx=2, pady=2)

# Add toolbar to root
toolbar.pack(side=tk.TOP, fill=tk.X)

# ****************  Create a status bar  *****************

statusBar = tk.Label(root, text='Preparing to do nothing...', bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusBar.pack(side=tk.BOTTOM, fill=tk.X)


root.mainloop()
