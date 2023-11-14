from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
from pprint import pprint
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
db = SQLAlchemy()
db.init_app(app)
Bootstrap5(app)


class RatingForm(FlaskForm):
    rating = FloatField(label='Your Rating Out Of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField()


class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label="Add movie")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


@app.route("/")
def home():
    # db.create_all()
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for i in range(len(movies)):
        ranking = len(movies) - i
        movies[i].ranking = ranking
        db.session.commit()
    ranked=db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars().all()
    return render_template("index.html", movies=ranked)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        params = {"api_key": "ed7b446efc993c810e1e42b86c72cbe7",
                  "query": title}
        response = requests.get(url='https://api.themoviedb.org/3/search/movie',  params=params)
        data = response.json()['results']
        pprint(data)
        return render_template("select.html", data=data)
    return render_template("add.html", form=form)


@app.route("/delete")
def delete():
    movie_id = request.args['id']
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie)
    db.session.commit()
    return redirect("/")


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    form = RatingForm()
    if form.validate_on_submit():
        movie = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        movie.rating = request.form["rating"]
        movie.review = request.form["review"]
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", form=form)


@app.route("/details")
def details():
    id = request.args["id"]

    params = {
        "api_key": "ed7b446efc993c810e1e42b86c72cbe7"
    }
    response = requests.get(f"https://api.themoviedb.org/3/movie/{id}", params=params)
    data = response.json()
    print(data)
    movie = Movie(
        title=data['title'],
        img_url="https://image.tmdb.org/t/p/w500" + data["poster_path"],
        year=data['release_date'].split('-')[0],
        description=data['overview']
        # ranking=4,
        # review="Loved it",
        # rating=10
        )
    db.session.add(movie)
    db.session.commit()
    select_movie = db.session.execute(db.select(Movie).where(Movie.title == data["title"])).scalar()
    movie_id = select_movie.id
    return redirect(f"/edit/{movie_id}")


if __name__ == '__main__':
    app.run(debug=True)
