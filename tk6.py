import tkinter as tk


class MyButtons:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.printButton = tk.Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=tk.LEFT)

        self.quitButton = tk.Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=tk.LEFT)

    def printMessage(self):
        print('This things works!!!')


root = tk.Tk()
byButts = MyButtons(root)

root.mainloop()