from tkinter import *
from tkinter import messagebox
import pandas as pd
import csv
import random


LIGHT_GREEN = "#addec7"
FONT_NAME = "Ariel"

#----------------------------------- WORD DISPLAY --------------------------------------------------------------#

class OpenFile:
    def __init__(self):
        self.csv_file = pd.read_csv("words.csv", delimiter=",", dtype=str, encoding="latin1")
        self.file = self.csv_file.iloc[:, 1:]  # drop first column
        self.rows = self.file.values.tolist()
        self.random_select = random.choices(self.rows, k=1)

    def german_word(self):
        return self.random_select[0][0]

    def translated_word(self):
        return self.random_select[0][1]

open_file = OpenFile()

generate_german_word = open_file.german_word()
print(generate_german_word)


#---------------------- UI SETUP  ------------------------------------------------------------------------------#
window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=20, bg=LIGHT_GREEN)


# ------------------------------- CANVAS SETUP -----------------------------------------------------------------#
canvas = Canvas(height=560, width=800, bg=LIGHT_GREEN, highlightthickness=0)
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
wrong_img = PhotoImage(file="wrong.png")
right_img = PhotoImage(file="right.png")

# #front image
front_canvas = canvas.create_image(400, 300, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)

# #back image
# back_canvas = canvas.create_image(400, 300, image=back_img)
# canvas.grid(column=1, row=1, columnspan=2)

#------------------- Create canvas text ----------------------------------------
# Display the word "Deutsch" on the flash card
display_german_text = canvas.create_text(400, 263, text=generate_german_word, fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Display flash card word
display_language_deutsch = canvas.create_text(400, 120, text="Deutsch", fill="black", font=(FONT_NAME, 30, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

#---------------------------------------- BUTTON CANVAS SETUP ----------------------------------------------------#
wrong_btn_canvas = Canvas(height=150, width=150, bg=LIGHT_GREEN, highlightthickness=0)
#wrong button image
wrong_btn_canvas.create_image(50, 70, image=wrong_img)
wrong_btn_canvas.grid(column=0, row=1)

#---------------------------------------- BUTTON CANVAS SETUP ----------------------------------------------------#
right_btn_canvas = Canvas(height=150, width=150, bg=LIGHT_GREEN, highlightthickness=0)
#wrong button image
right_btn_canvas.create_image(90, 70, image=right_img)
right_btn_canvas.grid(column=1, row=1)
#----------------------------------- BUTTONS SETUP -------------------------------------------------------------#



















window.mainloop()