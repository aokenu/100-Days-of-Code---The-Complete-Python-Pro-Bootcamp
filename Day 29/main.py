from tkinter import *
from tkinter import messagebox
import csv
import string
import random
import pyperclip
import json



# ------------------------------------ PASSWORD GENERATOR ------------------------------------------------------------ #
numbers = list(string.digits)
alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
special_chars = list(string.punctuation)

char_pool = alphabet + numbers + special_chars

def generate_password():
    password_entry.delete(0, END)
    random_pass = random.choices(char_pool, k=15)  # choose 15 random characters
    passwd = ''.join(random_pass)  # join them into a string
    password_entry.insert(0, passwd)
    pyperclip.copy(passwd)


# ----------------------------------- SAVE PASSWORD ------------------------------------------------------------------ #
# function to clear entry text
def clear_fields():
    website_entry.delete(0, END)
    password_entry.delete(0, END)

    # function to get and save details entered into the entry fields
def get_info():
    get_web_info = website_entry.get().title()
    get_email_info = email_entry.get()
    get_pass_info = password_entry.get()
    new_data = {
        get_web_info: {
        "email": get_email_info,
        "password": get_pass_info,
    }
    }

    if len(get_web_info) == 0 or len(get_pass_info) == 0 or len(get_web_info) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# -------------------------------------FIND PASSWORD ------------------------------------------------------------------#
def find_password():
    web_search = website_entry.get().title()
    if len(web_search) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any field empty")
    else:
        try:
            with open("data.json", "r") as search_file:
                # Reading old data
                working_file = json.load(search_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Missing File", message="No Such Data File Found!")

        else:
            try:
                # iterate over the records in the working files to check if the search entry match any existing record
                if web_search in working_file:
                    email = working_file[web_search]["email"]
                    password = working_file[web_search]["password"]
                    messagebox.showinfo(title=web_search, message=f"Email: {email}\nPassword: {password}")
                else:
                    messagebox.showinfo(title="Oops", message="No details for the website exists!")
            finally:
                website_entry.delete(0, END)




# ------------------------------------ UI SETUP ---------------------------------------------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


#-------------------------------------- Canvas ------------------------------------------------------------------------#
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#-------------------------------------------- Labels ------------------------------------------------------------------#
# define a label for the website field
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=2)


# define a label for the website field
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=2)

# define a label for the website field
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=2)



# Create a Frame to Align "Website" Input and the "Search" Button
website_frame = Frame(window)
website_frame.grid(row=1, column=1, columnspan=2)

# "Website" entry field inside the Frame
website_entry = Entry(website_frame, width=24)
website_entry.grid(row=0, column=0, padx=9, pady=2)

#"Search" button inside the Frame
search_btn = Button(website_frame, text="Search", width=14, command=find_password)
search_btn.grid(row=0, column=1,padx=10, pady=2)


#---------------------------------------- Entry Field -----------------------------------------------------------------#
# create a text field for the email/username
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2, pady=2)
email_entry.insert(0, "tkguru@gmail.com")


# Create a Frame to Align Password Input and Button
password_frame = Frame(window)
password_frame.grid(row=3, column=1, columnspan=2)

# Password entry field inside the Frame
password_entry = Entry(password_frame, width=24)
password_entry.grid(row=0, column=0, padx=9, pady=2)

#Password button inside the Frame
gen_passwd_btn = Button(password_frame, text="Generate Password", width=14, command=generate_password)
gen_passwd_btn.grid(row=0, column=1,padx=10, pady=2)


#--------------------------------------------- Buttons ----------------------------------------------------------------#

# create a button for saving generated password
add_passwd_btn = Button(text="Add", width=38, command=get_info)
add_passwd_btn.grid(column=1, columnspan=2, row=4, pady=2)




















window.mainloop()