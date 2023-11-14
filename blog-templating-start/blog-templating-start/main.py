from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get('https://api.npoint.io/c790b4d5cab5'
                        '8020d391')
all_blogs = response.json()


@app.route('/')
def home():
    return render_template("index.html", blogs=all_blogs)


@app.route('/post/<blog_id>')
def get_blog(blog_id):
    return render_template('post.html', id=int(blog_id), blogs=all_blogs)


if __name__ == "__main__":
    app.run(debug=True)
