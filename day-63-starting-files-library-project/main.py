from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -wtr requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.id))
    all_books = result.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form['name'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect('/')
    return render_template("add.html")


@app.route("/edit/id=<book_id>", methods=['GET', 'POST'])
def edit(book_id):
    book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    if request.method == "POST":
        book.rating = request.form['new_rating']
        db.session.commit()
        return redirect('/')
    return render_template("edit.html", book=book)


@app.route("/delete")
def delete():
    with app.app_context():
        book_id = request.args.get("id")
        book = db.get_or_404(Book, book_id)
        db.session.delete(book)
        db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)


