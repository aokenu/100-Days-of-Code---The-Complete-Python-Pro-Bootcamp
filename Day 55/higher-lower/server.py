from flask import Flask
import random

# initializing a Flask app
app = Flask(__name__)



        


# this defines the root route of the Flask app
@app.route('/')
def home_route():
    return '<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'




# red text decorator
def red_decorator(func):
    def color_wrapper(**kwargs):
        return f"<h1 style='color: red'>{func(**kwargs)}</h1>"
    return color_wrapper

def random_number():
    num = random.randint(1, 50)
    return num


@app.route('/<int:number>')
@red_decorator
def get_number(number):
    rand_num = random_number()
    if number < rand_num:
        return (f"{number}<p></p>"
                f"Oops!Too low, try again. The random number is:{rand_num}<p></p>"
                f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'")
    
    elif number > rand_num:
        return (f"{number}<p></p>"
                f"Oops!Too high, try again. The random number is:{rand_num}<p></p>"
                f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'")
    
    else:
        return (f"{number}<p></p>"
                f"Good! That's correct.<p></p>"
                f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'")

 



if __name__ == '__main__':
    app.run(debug=True)