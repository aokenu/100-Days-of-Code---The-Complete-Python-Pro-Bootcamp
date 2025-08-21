from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR )

        # Create a text box
        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=(10) )
        self.label.grid(row=0, column=1)

        self.left_image = PhotoImage(file="./images/true.png")
        self.right_image = PhotoImage(file="./images/false.png")

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        # Create the two buttons
        self.left_button = Button(image=self.left_image, highlightthickness=0)
        self.left_button.grid(row=3, column=0, padx=20, pady=20)
        self.right_button = Button(image=self.right_image, highlightthickness=0)
        self.right_button.grid(row=3, column=1, padx=20, pady=20)





        self.window.mainloop()