from tkinter import *

window = Tk()
window.title("Column Exercise")

window.minsize(width=800, height=800)
window.config(padx=100, pady=50)

# row 0 column 0
label_1 = Label(text="Row 0 Column 0")
label_1.grid(row=0, column=0)

# row 1 column 1
button_1 = Button(text="Row 1 Column 1")
button_1.grid(row=1, column=1)

# row 2 column 0
button_2 = Button(text="Row 2 Column 0")
button_2.grid(row=2, column=0)

# row 0 column 2
entry_1 = Entry()
entry_1.grid(row=0, column=2)
entry_1.insert(END, "Default Text")


window.mainloop()
