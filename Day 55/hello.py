from flask import Flask

app = Flask(__name__)

# decorator to make text big
def make_big(func):
    def enhanced_text():
        return f"<h1>{func()}</h1>" 
    return enhanced_text

# decorator to make text bold
def make_bold(func):
    def enhanced_text():
        return f"<b>{func()}</b>"
    return enhanced_text

# decorator to emphasize a text
def make_emphasis(func):
    def enhanced_text():
        return f"<em>{func()}</em>"
    return enhanced_text


# decorator to underline a text
def make_underlined(func):
    def enhanced_text():
        return f"<u>{func()}</u>"
    return enhanced_text

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/bye')
@make_big
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye'

#
# @app.route('/username/<username>')
# def greet(name):
#     return f"Hello {name}"
#


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return (f'<h2 style="text-align: center">Hello there {name}, you are {number} years old</h2>'
            f'<p>This is a paragraph</p>'
            f'<img src ="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWtpYm91czJ0NnA0dXI3aGVicDZobHF0ZjNkbmRyYnVpaHl4djluaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LMn7PRCVDcnvO/giphy.gif" width=600px>'            )




if __name__ == "__main__":
    app.run(debug=True)