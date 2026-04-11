from flask import Flask, render_template
import requests, json


app = Flask(__name__)


@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    response.raise_for_status()
    blog_response = response.json()
    return render_template("index.html", home_post=blog_response)


@app.route('/post/<blog_id>')
def blog(blog_id):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(url)
    all_posts = blog_response.json()
    return render_template('post.html', posts=all_posts, text_id=blog_id)




if __name__ == "__main__":
    app.run(debug=True)
