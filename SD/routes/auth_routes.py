from flask import Blueprint, render_template, request, redirect, session, flash
from application.services.auth_service import login_user, register_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user, errors = login_user(request.form)
        if user:
            session["user"] = {
                "id": user["id"],
                "full_name": user["full_name"],
                "username": user["username"],
                "email": user["email"],
                "role": user["role"]
            }
            return redirect("/dashboard")
        for error in errors:
            flash(error, "error")
    return render_template("login.html")

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        success, messages = register_user(request.form)
        if success:
            flash(messages[0], "success")
            return redirect("/")
        for message in messages:
            flash(message, "error")
    return render_template("signup.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect("/")
