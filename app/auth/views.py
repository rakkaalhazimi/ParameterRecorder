from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user

from app import login_manager
from app.auth import models
from app.auth.services import validate_registration


auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = models.User.get(email=email, password=password)
        
        if user:
            flash("Login success")
            login_user(user)
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

        is_valid = validate_registration(email, password, confirm_password)

        if is_valid:
            flash("Register success")
        else:
            flash("Register failed")
        
        return redirect(url_for("auth.login"))


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))



@login_manager.user_loader
def load_user(user_id):
    return models.User.get(id=user_id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for("auth.login"))