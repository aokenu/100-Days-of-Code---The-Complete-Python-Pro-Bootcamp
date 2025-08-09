from tkinter import *
from tkinter import messagebox
import csv
import string
import random
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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


# ---------------------------- SAVE PASSWORD ------------------------------- #
# function to clear entry text
def clear_fields():
    website_entry.delete(0, END)
    password_entry.delete(0, END)

    # function to get and save details entered into the entry fields
def get_info():
    get_web_info = website_entry.get()
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
                # Updating new data
                data.update(new_data)
        except Exception:
            print("No such file exist")
            data = {}
        except Exception:
            with open("data.json", "x") as data_file:
                data = {}
                # Reading old data
                data = json.load(data_file)
                # Updating new data
                data.update(new_data)
        else:
            print("None")


        with open("data.json", "w") as data_file:
            #saving the updated data
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


#---------------------Canvas----------------------------
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#--------------------Labels-----------------------------
# define a label for the website field
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=2)


# define a label for the website field
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=2)

# define a label for the website field
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=2)


#-----------------Entry Field---------------------------
# create a text field for the website
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2, pady=2)
website_entry.focus()

# create a text field for the email/username
email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2, pady=2)
email_entry.insert(0, "tkguru@gmail.com")



# Create a Frame to Align Password Input and Button
password_frame = Frame(window)
password_frame.grid(row=3, column=1, columnspan=2)

password_entry = Entry(password_frame, width=24)
password_entry.grid(row=0, column=0, padx=9, pady=2)


#-------------------Buttons-----------------------------
gen_passwd_btn = Button(password_frame, text="Generate Password", width=14, command=generate_password)
gen_passwd_btn.grid(row=0, column=1,padx=10, pady=2)

# create a button for saving generated password
add_passwd_btn = Button(text="Add", width=38, command=get_info)
add_passwd_btn.grid(column=1, columnspan=2, row=4, pady=2)


















window.mainloop()