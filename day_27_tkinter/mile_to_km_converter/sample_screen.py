import tkinter

FONT = ("Arial", 24, "bold")

window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=800, height=600)

# label
"""Construct a label widget with the parent MASTER.
def __init__(self, master=None, cnf={}, **kw):

    STANDARD OPTIONS

    activebackground, activeforeground, anchor,
    background, bitmap, borderwidth, cursor,
    disabledforeground, font, foreground,
    highlightbackground, highlightcolor,
    highlightthickness, image, justify,
    padx, pady, relief, takefocus, text,
    textvariable, underline, wraplength

    WIDGET-SPECIFIC OPTIONS

    height, state, width

"""
# my_label = tkinter.Label(text="TEXT")

# configuration dictionary mapping
default_font = {"text": "With Dict", "font": ("Arial", 24, "bold")}
my_label = tkinter.Label(cnf=default_font, font=("Arial", 40, "bold"))
""" pack = configure = config = pack_configure """
"""Pack a widget in the parent widget. Use as options:
        after=widget - pack it after you have packed widget
        anchor=NSEW (or subset) - position widget according to
                                  given direction
        before=widget - pack it before you will pack widget
        expand=bool - expand widget if parent size grows
        fill=NONE or X or Y or BOTH - fill widget if widget grows
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
"""
my_label.pack()





window.mainloop()
