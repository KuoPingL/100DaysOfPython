from tkinter import * # this is for all Classes
import tkinter.ttk as ttk
from tkinter import messagebox
import pandas as pd
import os
from util.password_generator import PasswordGenerator
import json
from util.json_manager import JsonManager


FILE_CSV = "password.csv"
FILE_TXT = "password.txt"
FILE_JSON = "password.json"
COLUMN_USERNAME = "username"
COLUMN_PASSWORD = "password"
COLUMN_WEBSITE = "website"

# ---------------------------- CUSTOM PASSWORD ENTRY ---------------------------- #
# class PasswordEntry(Frame):
#     def __init__(self, parent, title, **kwargs):
#         super(PasswordEntry, self).__init__(parent, **kwargs)
#         self.label = Label(text=title, anchor="e")
#         self.entry = Entry(width=21, show="*")
#         self.showImage = PhotoImage("show_password.png")
#         self.hideImage = PhotoImage("hide_password.png")
#         self.show_hide_button = Button(image=self.hideImage)
#         self.__isPasswordHidden = True
#
#         self.label.grid()
#
#     def trigger_password(self):
#         self.__isPasswordHidden = not self.__isPasswordHidden
#         self.entry.config(image=self.hideImage if self.__isPasswordHidden else self.showImage)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = PasswordGenerator.generate_password()
    password_input.delete(0, END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get()
    username = email_input.get()
    password = password_input.get()

    save_password_txt(website=website, username=username, password=password)

def save_password_csv(website: str, username: str, password: str):

    website = website.strip()
    username = username.strip()
    password = password.strip()

    if len(username) == 0 or len(password) == 0 or len(website) == 0:
        print(f"INVALID WEBSITE, USERNAME and VALUE : ${website} ,${username}, ${password}")
        return

    if not os.path.isfile(FILE_CSV):
        # does not contain file
        df = pd.DataFrame()
        df[COLUMN_WEBSITE] = []
        df[COLUMN_USERNAME] = []
        df[COLUMN_PASSWORD] = []
        df.to_csv(FILE_CSV)

    df = pd.read_csv(FILE_CSV)


def save_password_txt(website: str, username: str, password: str):

    if len(username) == 0 or len(password) == 0 or len(website) == 0:
        print(f"INVALID WEBSITE, USERNAME and VALUE : ${website} ,${username}, ${password}")
        return

    is_ok = messagebox.askokcancel(f"{website}", message=f"These are the details you entered: "
                                                        f"\nEMAIL/USERNAME: {username} \nPASSWORD: {password} "
                                                        f"\nIs it ok to save?")

    # if is_ok:
    #     with open(FILE_TXT, mode="a") as f:
    #         f.write(f"{website} | {username} | {password}\n")
    #         website_input.delete(0, END)
    #         password_input.delete(0, END

    # JSON
    new_data = {
        website: {
            COLUMN_USERNAME: username,
            COLUMN_PASSWORD: password
        }
    }

    jm = JsonManager(FILE_JSON)
    if is_ok:
        # with open(FILE_JSON, mode="r") as data_file:
        #     # fetch old data
        #     data = json.load(fp=data_file)
        #     print(f"data = {data}")
        #     # update with new data
        #     data.update(new_data)
        #
        # with open(FILE_JSON, mode="w") as data_file:
        #     # saving updated data
        #     json.dump(obj=data, fp=data_file, indent=4)
        #     website_input.delete(0, END)
        #     password_input.delete(0, END)

        # try:
        #     with open(FILE_JSON, mode="r") as f:
        #         data = json.load(fp=f)
        # except FileNotFoundError:
        #     with open(FILE_JSON, mode="w") as f:
        #         json.dump(new_data, fp=f, indent=4)
        # else:
        #     data.update(new_data)
        #
        #     with open(FILE_JSON, mode="w") as f:
        #         json.dump(data, fp=f, indent=4)
        # finally:
        #     website_input.delete(0, END)
        #     password_input.delete(0, END)


        # option + command + L ... format JSON
        jm.update(new_data)
        website_input.delete(0, END)
        password_input.delete(0, END)



def search_password():
    website = website_input.get()
    website = website.strip()
    jm = JsonManager(FILE_JSON)
    data = jm.load()

    try:
        data = data[website]
        username = data[COLUMN_USERNAME]
        password = data[COLUMN_PASSWORD]
    except KeyError:
        messagebox.showerror(title="Error", message=f"No info were found on {website}")
    else:
        messagebox.showinfo(title=f"Info: {website}",
                            message=f"{COLUMN_USERNAME.title()}: {username}\n"
                                    f"{COLUMN_PASSWORD.title()}: {password}")





# def get_password(key: str):

def trigger_show_hide_password():
    global isPasswordHidden
    isPasswordHidden = not isPasswordHidden
    password_button_icon.config(image=password_hide_icon if isPasswordHidden else password_show_icon)
    password_input.config(show="*" if isPasswordHidden else "")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ---------------------------- CANVAS ---------------------------- #
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ---------------------------- WEBSITE ---------------------------- #
website_label = Label(text="Website : ", anchor="e", pady=2)
website_input = Entry(width=21)
website_button = Button(text="Search", command=search_password)

website_label.grid(row=1, column=0, sticky="ew", pady=2)
website_input.grid(row=1, column=1)
website_button.grid(row=1, column=2, sticky="ew")

website_input.insert(0, "coolkid@mymail.com")

website_input.focus()

# ---------------------------- EMAIL/USERNAME ---------------------------- #
email_label = Label(text="Email/Username : ", pady=2, anchor="e")
email_input = Entry(width=35)

email_label.grid(row=2, column=0, sticky="ew", pady=2)
email_input.grid(row=2, column=1, columnspan=2)

# ---------------------------- PASSWORD ---------------------------- #
password_label = Label(text="Password : ", anchor="e")
password_input = Entry(width=21, show="*")

password_button = Button(text="Generate Password", command=generate_password)

password_label.grid(row=3, column=0, sticky="ew", pady=2)
password_input.grid(row=3, column=1)
password_button.grid(row=3, column=2)

# ---------------------------- PASSWORD ICON ---------------------------- #
isPasswordHidden = True

icon_width = 15
power = 5

password_show_icon = PhotoImage(file="show_password.png")
password_hide_icon = PhotoImage(file="hide_password.png")

print(password_show_icon.width())
print(password_show_icon.height())

password_show_icon = password_show_icon.subsample(2**power)
password_hide_icon = password_hide_icon.subsample(2**power)

print(512/(2**power))

password_button_icon = Button(image=password_hide_icon, command=trigger_show_hide_password, foreground="white")

print(password_show_icon.width())
print(password_show_icon.height())
#
# print(password_input.winfo_reqheight())
rely = (password_input.winfo_reqheight() - password_hide_icon.height())/password_input.winfo_reqheight()/2.0
# print(rely)
password_button_icon.place(in_=password_input, relx=(210 - 5 - password_hide_icon.width())/210, rely=0.0)
# ttk.Style().configure('pad.TEntry', padding='10 1 10 1')
# password_input.config(style='pad.TEntry')

# ---------------------------- ADD ---------------------------- #
add_button = Button(text="Add", width=36, pady=5, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=2)




window.mainloop()
