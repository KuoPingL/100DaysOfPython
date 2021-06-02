from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import time

FONT_LANGUAGE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"


current_letter = dict()
current_task_id = None
data: pd.DataFrame = None


def image_path(name: str) -> str:
    return f"images/{name}"


def ask_to_restart_data():
    is_ok = messagebox.askokcancel(title="Well Done", message="Do you wish to review the list?")
    # window.update()
    if is_ok:
        prepare_data()
        right_button.config(command=remove_word)
        wrong_button.config(command=fetch_new_word)
    else:
        window.destroy()
        return


def prepare_data():
    global data

    data = pd.read_csv("data/french_words.csv")
    data.to_csv("data/words_to_learn.csv", index=False)
    data = pd.read_csv("data/words_to_learn.csv")

    fetch_new_word()


def fetch_new_word():
    global current_letter, current_task_id, data, is_card_front

    is_card_front = True

    if current_task_id is not None:
        window.after_cancel(current_task_id)

    if data is None:
        try:
            data = pd.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            prepare_data()

    # data = pd.read_csv("data/french_words.csv")
    # [(  0, 'partie', 'part') (  1, 'histoire', 'history') ...]
    # print(len(data.to_records()))
    # [{'French': 'partie', 'English': 'part'}, ... ]
    print(data.to_dict(orient="records"))

    if len(data) == 0:
        card_bg.itemconfig(card_title, text="Well Done", fill="black")
        card_bg.itemconfig("word", text="You have learned \nwhole stack of words", fill="black")
        right_button.config(command=ask_to_restart_data)
        wrong_button.config(command=ask_to_restart_data)
        return

    # default card
    card_bg.itemconfig("background", image=card_front)

    current_letter = random.choice(data.to_dict(orient="records"))
    key = list(current_letter.keys())[0]
    card_bg.itemconfig(card_title, text=key, fill="black")
    card_bg.itemconfig("word", text=current_letter[key], fill="black")

    # this will hold the main thread
    # time.sleep(3)
    print("3 SECONDs")
    current_task_id = window.after(3000, flip_the_card)


def remove_word():
    global current_letter, data

    print(type(data))

    if len(current_letter.keys()):
        print(current_letter)
        index = data.index[data.French == current_letter["French"]].tolist()
        # data = data.drop(index)
        data.drop(index, inplace=True)
        data.to_csv("data/words_to_learn.csv", index=False)
    fetch_new_word()


def flip_the_card(is_to_front: bool = False):
    global current_letter, current_task_id

    # flip
    image = card_front if is_to_front else card_back
    # image = (card_back, card_front)[is_to_front] # (if true do this, else do this) [ Bool ]
    card_bg.itemconfig("background", image=image)

    # https://book.pythontips.com/en/latest/ternary_operators.html
    color = ("white", "black")[is_to_front]
    # index = (1, 0)[is_to_front]
    key = list(current_letter.keys())[0 if is_to_front else 1]
    card_bg.itemconfig("title", text=key, fill=color)
    card_bg.itemconfig("word", text=current_letter[key], fill=color)


is_card_front = True


def flip_card_by_event(event):
    global is_card_front, current_task_id

    if current_task_id is not None:
        print("Gone in 3 SECONDs")
        window.after_cancel(current_task_id)

    is_card_front = not is_card_front
    flip_the_card(is_card_front)


# Window
window = Tk()
window.wm_title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# images
# RuntimeError: Too early to create image: no default root window
card_back = PhotoImage(file=image_path("card_back.png"))
card_front = PhotoImage(file=image_path("card_front.png"))
right = PhotoImage(file=image_path("right.png"))
wrong = PhotoImage(file=image_path("wrong.png"))

# card_back = card_back.resize((400, 240))

# background

# bg_image = Canvas(window, bg=BACKGROUND_COLOR)
# bg_image.pack(fill=BOTH)

# card
# card_bg = Label(bg_image, image=card_front, height=526, width=800)
# card_bg.pack(fill=BOTH, padx=50, pady=50)

card_bg = Canvas(window, height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg.create_image(400, 526/2, image=card_front, tags="background")
card_bg.grid(row=0, column=0, columnspan=2)
card_title = card_bg.create_text(400, 150, text="", font=FONT_LANGUAGE, tags="title")
card_bg.create_text(400, 263, text="", font=FONT_WORD, tags="word")

# https://stackoverflow.com/questions/29211794/how-to-bind-a-click-event-to-a-canvas-in-tkinter
card_bg.bind("<Button-1>", flip_card_by_event)

# # title
# language_label = Label(card_bg, text="title", font=FONT_LANGUAGE)
# language_label.place(x=400, y=150)
#
# # word
# word_label = Label(card_bg, text="word", font=FONT_WORD)
# word_label.place(x=400, y=263)

# right / wrong
right_button = Button(window, image=right, highlightthickness=0, command=remove_word)
wrong_button = Button(window, image=wrong, highlightthickness=0, command=fetch_new_word)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

fetch_new_word()

window.mainloop()

