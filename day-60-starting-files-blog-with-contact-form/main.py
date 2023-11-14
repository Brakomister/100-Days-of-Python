from flask import Flask, render_template, request
import requests
import smtplib

email = "kbrako.asante@gmail.com"
password = "dgsagvrraeuebojp"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)


# # USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
# posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def get_all_posts():
#     return render_template("index.html", all_posts=posts)
#
#
# @app.route("/about")
# def about():
#     return render_template("about.html")
#
#
# @app.route("/contact", methods=["POST", "GET"])
# def contact():
#     if request.method == "POST":
#         to_email = request.form["email"]
#         message = request.form["message"]
#         connection.sendmail(from_addr=email, to_addrs=to_email,
#                             msg=message)
#         return render_template("contact.html", title="Message successfully sent")
#     return render_template("contact.html", title="Contact Me")
#
#
# @app.route("/post/<int:index>")
# def show_post(index):
#     requested_post = None
#     for blog_post in posts:
#         if blog_post["id"] == index:
#             requested_post = blog_post
#     return render_template("post.html", post=requested_post)
#
#
#
# if __name__ == "__main__":
#     app.run(debug=True, port=5001)
