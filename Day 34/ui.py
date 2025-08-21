from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.false_img = PhotoImage(file="images/false.png")
        self.true_img = PhotoImage(file="images/true.png")

        score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR,  font=("Arial", 12, "bold"))
        score_label.grid(row=0, column=1)

        canvas = Canvas(width=300, height=250, bg="white")
        slef.question = canvas.create_text(
            150, 125,
            text="Some text here",
            width=280,
            font=("Arial", 15, "bold")
            )
        canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true_btn = Button(image=self.true_img)
        true_btn.grid(row=2, column=0, padx=20, pady=20)

        false_btn = Button(image=self.false_img)
        false_btn.grid(row=2, column=1, padx=20, pady=40)



        self.window.mainloop()



