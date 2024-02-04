from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = response.json()
    return render_template("index.html", blogs=blogs)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/contact/<int:id>')
def get_blog(id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = response.json()
    return render_template("post.html", blogs=blogs, id=id)


@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    email = request.form.get('email')
    phoneno = request.form.get('phone')
    print(f"Received data: \nname - {name}\nEmail - {email}\nPh.No - {phoneno}")

# @app.route('/blog/<int:id>')
# def get_blog(id):
#     response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
#     blogs = response.json()
#     return render_template("post.html", blog_id=id, blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)
