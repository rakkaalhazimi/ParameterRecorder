from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user

from app import login_manager
from app.auth.models import db, User


auth = Blueprint("auth", __name__, url_prefix="/auth")


@login_manager.user_loader
def load_user(user_id):
    print(f"User id: {user_id}")
    return User.query.get(user_id)


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = db.session.execute(
            db.select(User)
              .where(User.email == email and User.password == password)).one()
        
        if login_user(user[0]):
            flash("Login success")
            return redirect(url_for("base.home"))

        return redirect(url_for("auth.login"))


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password == confirm_password:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Register success")
        
        else:
            flash("Register failed")
        
        return redirect(url_for("auth.login"))
