from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests
<<<<<<< HEAD
import json
from ui import QuizInterface

=======


>>>>>>> 6f0a0bcf2cf07156481035047b0a9452720e8448


URL = "https://opentdb.com/api.php"
parameter = {
    "amount": 10,
    "type": "boolean"
}

quiz_data = []

def get_data():
    global quiz_data
    # Pass parameters correctly
    response = requests.get(URL, parameter)

    # Convert to JSON
    data = response.json()
    quiz_data = data["results"]


get_data()


question_bank = []
for question in quiz_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

