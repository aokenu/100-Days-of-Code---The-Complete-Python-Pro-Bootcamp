from flask import Flask, render_template
from datetime import datetime
import requests


# create a flask app
app = Flask(__name__)



# create a route
@app.route('/guess/<names>')
def guess(names):
    # getting the name and gender values from the genderize api
    url = f"https://api.genderize.io/?name={names}"
    api_response = requests.get(url)
    data = api_response.json()

    # getting the age value from the agify api
    url = f"https://api.agify.io/?name={names}"
    api_response_age = requests.get(url)
    age_data = api_response_age.json()

    name = data["name"]
    gender = data["gender"]
    age = age_data["age"]

    current_year = datetime.now().year
    return render_template('index.html', year=current_year, name=name, gender=gender, age=age)


@app.route('/blog')
def blog_post():
    url = "https://api.npoint.io/4d652f276bd4730bb65a"
    blog_response = requests.get(url)
    all_posts = blog_response.json()
    return render_template('blog.html', posts=all_posts)

# run the flask app
if __name__ == '__main__':
    app.run(debug=True)