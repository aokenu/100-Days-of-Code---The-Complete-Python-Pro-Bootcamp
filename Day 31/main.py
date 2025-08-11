from tkinter import *
from tkinter import messagebox
import pandas as pd
import time
import random

LIGHT_GREEN = "#addec7"
FONT_NAME = "Ariel"
#----------------------------------- WORD DISPLAY --------------------------------------------------------------#

class OpenFile:
    def __init__(self):
        self.csv_file = pd.read_csv("words.csv", delimiter=",", dtype=str, encoding="latin1")
        self.file = self.csv_file.iloc[:, 1:]  # drop first column
        self.rows = self.file.values.tolist()
        self.random_select = None

    def shuffle_word(self):
        self.random_select = random.choice(self.rows)

    def german_word(self):
        return self.random_select[0]

    def translated_word(self):
        return self.random_select[1]

open_file = OpenFile()

open_file.shuffle_word()
generate_german_word = open_file.german_word()
translate_to_english = open_file.translated_word()

#---------------------- UI SETUP  ------------------------------------------------------------------------------#
window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=20, bg=LIGHT_GREEN)

# ------------------------------- CANVAS SETUP -----------------------------------------------------------------#
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
wrong_img = PhotoImage(file="wrong.png")
right_img = PhotoImage(file="right.png")


def flash_card():
    global canvas, display_text, display_language, front_img_id
    canvas = Canvas(height=560, width=800, bg=LIGHT_GREEN, highlightthickness=0)

    # #front image
    front_img_id = canvas.create_image(400, 300, image=front_img)
    canvas.grid(column=0, row=0, columnspan=2)

    #------------------- Create canvas text ----------------------------------------
    # Display the word "Deutsch" on the flash card
    display_text = canvas.create_text(400, 263, text=generate_german_word, fill="black", font=(FONT_NAME, 60, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    # Display flash card word
    display_language = canvas.create_text(400, 120, text="Deutsch", fill="black", font=(FONT_NAME, 30, "italic"))
    canvas.grid(column=0, row=0, columnspan=2)

def flip_card():
    canvas.itemconfig(front_img_id, image=back_img)
    canvas.itemconfig(display_text, text=open_file.translated_word(), fill="white")
    canvas.itemconfig(display_language, text="English", fill="white")

def update_card():
    open_file.shuffle_word()
    canvas.itemconfig(front_img_id, image=front_img)
    canvas.itemconfig(display_text, text=open_file.german_word(), fill="black")
    canvas.itemconfig(display_language, text="Deutsch", fill="black")
    window.after(3000, flip_card)

def wrong_answer():
    update_card()

def correct_answer():
    update_card()

#----------------------------------- BUTTONS SETUP -------------------------------------------------------------#
start_button = Button(image=wrong_img, command=wrong_answer)
start_button.grid(column=0, row=1)

start_button = Button(image=right_img, command=correct_answer)
start_button.grid(column=1, row=1)


flash_card()


window.after(3000, flip_card)
window.mainloop()