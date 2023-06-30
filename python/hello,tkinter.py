from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

# Create a StringVar for updating the label text
counter = StringVar()
counter.set("0")

#label that displays "victory points" above the two buttons
ttk.Label(frm, text="Victory Points").grid(column=0, row=0)

# function to increment the counter
def increment():
    counter.set(str(int(counter.get()) + 1))

# function to decrement the counter
def decrement():
    counter.set(str(int(counter.get()) - 1 if int(counter.get()) > 0 else 0))

#button that increases a counter when clicked
ttk.Button(frm, text="Add", command=increment).grid(column=1, row=0)

# button that decreases a counter when clicked
ttk.Button(frm, text="Subtract", command=decrement).grid(column=2, row=0)

# label that displays the counter
ttk.Label(frm, textvariable=counter).grid(column=3, row=0)

# maximize the window
root.state('zoomed')

root.mainloop()
