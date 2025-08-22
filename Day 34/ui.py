from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

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
            width= 280,
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        # Create the two buttons
        self.left_button = Button(image=self.left_image, highlightthickness=0, command=self.true_pressed)
        self.left_button.grid(row=3, column=0, padx=20, pady=20)
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.false_pressed)
        self.right_button.grid(row=3, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.left_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def score_board(self):
        global score
        if self.give_feedback:
            score += 1
            return score