from flask import Flask, render_template


# creating a falsk app
app = Flask(__name__)


def txt_decorator(func):
    def wrapper():
        return f"<h1>{func()}</h1>"
    return wrapper


# home route
@app.route('/')
@txt_decorator
def home():
    return "Welcome to my home page"


@app.route('/mysite')
def my_site():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)