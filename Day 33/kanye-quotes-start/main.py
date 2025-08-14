from tkinter import *
from tkinter import messagebox
import requests

URL = "https://api.kanye.rest"

def get_quote():
    global quote
    response = requests.get(URL)
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(display_quote, text=quote)


window = Tk()
back_image = PhotoImage(file="background.png")
logo = PhotoImage(file="kanye.png")

window.title("Kanye Quote")
window.config(padx=50, pady=20)

# setup for canvas
canvas = Canvas(height=500, width=400, highlightthickness=0)

# #front image
main_image = canvas.create_image(210, 220, image=back_image)
canvas.grid(column=0, row=0, columnspan=2)

display_quote = canvas.create_text(210, 220, text="Click the button for a Kanye quote", fill="black", font=("Ariel", 20, "italic"), width=200)
canvas.grid(column=0, row=0)


# Create button
btn = Button(image=logo, highlightthickness=0, command=get_quote)
btn.grid(column=0, row=1, columnspan=2)




window.mainloop()






