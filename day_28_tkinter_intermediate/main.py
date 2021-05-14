from tkinter import *
from PIL import Image, ImageTk
# from threading import Timer
# import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = 0.3

rep = 0
is_counting_down = False


# https://stackoverflow.com/questions/15193330/editing-text-in-tkinter
# https://junilearning.com/blog/coding-projects/make-countdown-timer-python/
# ---------------------------- TIMER RESET ------------------------------- #
def get_minute_seconds(sec: int):
    # floor division in Python returns the quotient, but rounds down to the nearest integer
    # math.floor(sec/60)
    return '{:02d}:{:02d}'.format(sec // 60, sec % 60)


def display_time(time):
    global canvas
    canvas.itemconfig(text=get_minute_seconds(time), tagOrId="time")


def reset_btn_pressed():
    global is_counting_down, rep
    rep = 0
    is_counting_down = False
    display_time(int(WORK_MIN * 60))
    title.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    # window.after(0, display_time, current_countdown)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_btn_pressed():
    global is_counting_down, rep

    work_min = int(WORK_MIN * 60)
    short_break = int(SHORT_BREAK_MIN * 60)
    long_break = int(LONG_BREAK_MIN * 60)

    rep += 1
    rep %= 9
    if rep == 0:
        check_label.config(text="")
        rep += 1

    if is_counting_down:
        return
    else:
        is_counting_down = True

        if rep % 8 == 0:
            count_down(long_break)
        elif rep % 2 == 0:
            count_down(short_break)
        else:
            title.config(text="Working", fg=GREEN)
            count_down(work_min)
    # global timer
    # print(timer)
    # print(timer.finished.is_set())
    # if timer and not timer.is_alive():
    #     timer.start()
    #     print(timer.finished.is_set())


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global is_counting_down, rep
    # cannot use sleep, because this will stop the mainloop
    # https://stackoverflow.com/a/34029360/9795114
    # time.sleep(1)
    if is_counting_down and count >= 0:
        display_time(count)
        window.after(1000, count_down, count - 1)
    else:
        is_counting_down = False
        work_min = int(WORK_MIN * 60)
        short_break = int(SHORT_BREAK_MIN * 60)
        long_break = int(LONG_BREAK_MIN * 60)

        next_rep = rep + 1

        if next_rep % 9 == 0:
            checks = "".join(["✓" for _ in range(0, next_rep // 2)])
            check_label.config(text=checks)
            # reset_btn_pressed()
        elif next_rep % 8 == 0:
            title.config(text="Break", fg=RED)
            display_time(long_break)
        elif next_rep % 2 == 0:
            title.config(text="Break", fg=PINK)
            display_time(short_break)
        else:
            title.config(text="Working", fg=GREEN)
            checks = "".join(["✓" for _ in range(0, next_rep // 2)])
            check_label.config(text=checks)
            display_time(work_min)

        canvas.update()


# timer = Timer(1, count_down)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Promodoro")
window.config(padx=100, pady=50, bg=YELLOW)

"""Construct a label widget with the parent MASTER.

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
# https://stackoverflow.com/questions/64290131/how-to-change-the-text-color-using-tkinter-label
title = Label(window, text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
title.pack()

# CANVAS
"""Construct a canvas widget with the parent MASTER.

        Valid resource names: background, bd, bg, borderwidth, closeenough,
        confine, cursor, height, highlightbackground, highlightcolor,
        highlightthickness, insertbackground, insertborderwidth,
        insertofftime, insertontime, insertwidth, offset, relief,
        scrollregion, selectbackground, selectborderwidth, selectforeground,
        state, takefocus, width, xscrollcommand, xscrollincrement,
        yscrollcommand, yscrollincrement."""
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# img = Image.open("dice.png")
# photo = ImageTk.PhotoImage(img)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"), tag="time")
canvas.pack()

# https://stackoverflow.com/a/47427091/9795114
frame = Frame(window, width=200, bg=YELLOW)
frame.pack(expand=True, fill=X)

"""Construct a button widget with the parent MASTER.

        STANDARD OPTIONS

            activebackground, activeforeground, anchor,
            background, bitmap, borderwidth, cursor,
            disabledforeground, font, foreground
            highlightbackground, highlightcolor,
            highlightthickness, image, justify,
            padx, pady, relief, repeatdelay,
            repeatinterval, takefocus, text,
            textvariable, underline, wraplength

        WIDGET-SPECIFIC OPTIONS

            command, compound, default, height,
            overrelief, state, width
        """
start_btn = Button(frame, text="Start", command=start_btn_pressed, highlightthickness=0)
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
start_btn.pack(side="left")

reset_btn = Button(frame, text="Reset", command=reset_btn_pressed, highlightthickness=0)
reset_btn.pack(side="right")

# bottom_frame = Frame(window)
# bottom_frame.pack()

check_label = Label(text="✓", fg=GREEN, bg=YELLOW)
check_label.pack(side="bottom")

reset_btn_pressed()
# print(TkVersion)

window.mainloop()
