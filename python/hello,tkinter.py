from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.pack()

#Label that displays "Victory Points Counter" in the window heading
root.title("Victory Points Counter")

# Create a StringVar for updating the label text
counter = StringVar()
counter.set("0")

# Frame for the buttons
button_frame = ttk.Frame(frm)
button_frame.pack()

#button that increases a counter when clicked
ttk.Button(button_frame, text="Add", command=lambda: counter.set(str(int(counter.get()) + 1))).pack(side=LEFT)

# button that decreases a counter when clicked, the button is red when the counter is 0
ttk.Button(button_frame, text="Subtract", command=lambda: counter.set(str(int(counter.get()) - 1 if int(counter.get()) > 0 else 0))).pack(side=LEFT)

# Button that resets the counter when clicked, positioned in the upper right corner
ttk.Button(button_frame, text="Reset", command=lambda: counter.set("0")).pack(side=LEFT)

#label that displays "Victory Points"
ttk.Label(frm, text="Victory Points", font=("Helvetica", 20)).pack()

# label that displays the counter
ttk.Label(frm, textvariable=counter, font=("Helvetica", 50, "bold" )).pack()

root.mainloop()
