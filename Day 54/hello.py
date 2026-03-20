from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


from markupsafe import escape

@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"