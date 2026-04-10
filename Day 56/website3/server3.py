from flask import Flask, render_template


# creating a falsk app
app = Flask(__name__)



# home route
@app.route('/')
def home():
    return "Welcome to Austine website"


# website route
@app.route('/mysite')
def main_site():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)