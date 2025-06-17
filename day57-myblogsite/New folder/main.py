from flask import Flask, render_template
import requests

app = Flask(__name__)

url = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:post_id>')
def blog(post_id):
    return render_template("post.html", post_id=post_id, posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)