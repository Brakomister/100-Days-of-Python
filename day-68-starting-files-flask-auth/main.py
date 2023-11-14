import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '5#y2L"F4Q8z'

# Configuring Flask Login
login_manager = LoginManager()
login_manager.init_app(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    return render_template("index.html", user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        password = generate_password_hash(password=request.form['password'],
                                          method='pbkdf2:sha256',
                                          salt_length=8
                                          )
        new_user = User(
            email=request.form['email'],
            name=request.form['name'],
            password=password
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template("secrets.html", user=current_user)
    return render_template("register.html", user=current_user)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if not user:
            flash("Wrong email entered.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            flash('Logged in successfully.')
            return render_template('secrets.html', user=current_user)
    return render_template("login.html", user=current_user)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", user=current_user)


@app.route('/logout')
def logout():
    logout_user(current_user)
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory='static',
        path='files/cheat_sheet.pdf',
    )


if __name__ == "__main__":
    app.run(debug=True)
