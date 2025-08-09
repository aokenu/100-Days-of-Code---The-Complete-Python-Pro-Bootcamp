from tkinter import *
from tkinter import messagebox
import csv


#---------------------- UI SETUP  ------------------------------------------------------------------------------#
window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50)


# ------------------------------- CANVAS SETUP -----------------------------------------------------------------#
canvas = Canvas(height=600, width=800)
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")

#front image
front_canvas = canvas.create_image(400, 300, image=front_img)
canvas.grid(column=1, row=1, columnspan=2)

#back image
back_canvas = canvas.create_image(400, 300, image=back_img)
canvas.grid(column=1, row=1, columnspan=2)



















window.mainloop()