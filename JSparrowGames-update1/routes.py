from ext import app, db
from flask import render_template, redirect, flash
from forms import RegisterForm, GameForm, LoginForm
from models import Game, Review, User
from flask_login import login_user, logout_user, login_required
from os import path
from flask import send_from_directory



@app.route("/")
def home():
    games = Game.query.all()
    return render_template("index.html",
                           games=games, role="admin")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        password=form.password.data)
        new_user.create()
        flash("You successfully became a pirate")
        return redirect("/")
    return render_template("register.html", form=form)



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user:
            login_user(user)
            flash("You successfully returned to piracy")
            return redirect("/")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/game/<int:game_id>")
def view_movie_details(game_id):
    game = Game.query.get(game_id)
    reviews = Review.query.filter(Review.game_id == game_id).all()
    return render_template("game_details.html",
                           game=game,
                           reviews=reviews)



@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory("static/downloads", filename, as_attachment=True)