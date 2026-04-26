from flask import Blueprint, render_template, session, redirect
from application.services.record_service import get_user_records

records_bp = Blueprint("records", __name__)

@records_bp.route("/records")
def records():
    if "user" not in session:
        return redirect("/")
    if session["user"]["role"] == "admin":
        return render_template("records.html", records=[], user=session["user"])
    return render_template("records.html", records=get_user_records(session["user"]["id"]), user=session["user"])
