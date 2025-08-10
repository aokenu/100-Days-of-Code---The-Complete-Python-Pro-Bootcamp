from tkinter import *
from tkinter import messagebox
import csv


#---------------------- UI SETUP  ------------------------------------------------------------------------------#
window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=20)


# ------------------------------- CANVAS SETUP -----------------------------------------------------------------#
canvas = Canvas(height=700, width=800)
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

#wrong button image
wrong_btn_canvas = canvas.create_image(200, 650, image=wrong_img)
canvas.grid(column=1, row=1)

#right button canvas
right_btn_canvas = canvas.create_image(600, 650, image=right_img)
canvas.grid(column=2, row=1)
#----------------------------------- BUTTONS SETUP -------------------------------------------------------------#



















window.mainloop()