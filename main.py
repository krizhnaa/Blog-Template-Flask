from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = response.json()
    return render_template("index.html", blogs=blogs)

@app.route('/blog/<id>')
def get_blog(id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = response.json()
    return render_template("post.html", blog_id=id, blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)
