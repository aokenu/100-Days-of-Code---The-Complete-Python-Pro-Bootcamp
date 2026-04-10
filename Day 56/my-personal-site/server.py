from flask import Flask, render_template

# this creates a Flask app
app = Flask(__name__)



@app.route('/')
def home_route():
    return render_template('index.html')



@app.route('/site')
def my_site():
    return render_template('website.html')


if __name__ == '__main__':
    app.run(debug=True)
