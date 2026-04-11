from flask import Flask, render_template


# create a flask app
app =  Flask(__name__)


# creating a home route
@app.route('/')
def home():
    return "Welcome to Austine's home page"

# website route
@app.route('/site')
def site():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)