from tkinter import *
from converter import Converter

FONT = ("Arial", 20, "bold")

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
# window.maxsize(width=500, height=300)
# window.geometry("510x310")
window.config(padx=5, pady=5)

# input text
entry = Entry(font=FONT, width=10, justify='center')
entry.grid(row=0, column=1)

# input label
entry_label = Label(font=FONT, text="Miles")
entry_label.grid(row=0, column=2)

# is equals to
is_equal_label = Label(font=FONT, text="is equals to ")
is_equal_label.grid(row=1, column=0)

# result_label
result_label = Label(font=FONT, text="0")
result_label.grid(row=1, column=1)

# km_label
km_label = Label(font=FONT, text="Km")
km_label.grid(row=1, column=2)


# button
def cal_button_action():
    km = round(Converter.convert_mile_to_km(float(entry.get())))
    result_label.config(text=f"{km}")


cal_button = Button(text="Calculate", font=FONT, command=cal_button_action)
cal_button.grid(row=2, column=1)

window.mainloop()
