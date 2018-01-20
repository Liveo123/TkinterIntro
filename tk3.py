import tkinter as tk
# import ttk

root = tk.Tk()

topFrame = tk.Frame(root)
topFrame.pack()
bottomFrame = tk.Frame(root)
bottomFrame.pack(side=tk.BOTTOM)

button1 = tk.Button(topFrame, text = 'button 1', bg='red' )
button2 = tk.Button(topFrame, text = 'button 2', bg='blue' )
button3 = tk.Button(topFrame, text = 'button 3', fg='green' )
button4 = tk.Button(bottomFrame, text = 'button 4', fg='purple' )

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()