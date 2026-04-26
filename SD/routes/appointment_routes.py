from flask import Blueprint, render_template, request, session, redirect, flash
from application.services.appointment_service import create_appointment, get_user_appointments, get_all_appointments_for_admin, complete_appointment_by_admin, cancel_appointment_by_client

appointment_bp = Blueprint("appointment", __name__)

@appointment_bp.route("/appointments", methods=["GET", "POST"])
def appointments():
    if "user" not in session:
        return redirect("/")
    user = session["user"]
    if request.method == "POST":
        if user["role"] == "admin":
            flash("Admin cannot create appointments.", "error")
            return redirect("/appointments")
        success, messages = create_appointment(request.form, user["id"])
        for message in messages:
            flash(message, "success" if success else "error")
        return redirect("/appointments")
    if user["role"] == "admin":
        return render_template("appointments_admin.html", appointments=get_all_appointments_for_admin(), user=user)
    return render_template("appointments_client.html", appointments=get_user_appointments(user["id"]), user=user)

@appointment_bp.route("/appointments/<int:appointment_id>/done", methods=["POST"])
def mark_done(appointment_id):
    if "user" not in session:
        return redirect("/")
    user = session["user"]
    success, messages = complete_appointment_by_admin(appointment_id, user["role"], request.form)
    for message in messages:
        flash(message, "success" if success else "error")
    return redirect("/appointments")

@appointment_bp.route("/appointments/<int:appointment_id>/cancel", methods=["POST"])
def mark_cancel(appointment_id):
    if "user" not in session:
        return redirect("/")
    user = session["user"]
    success, messages = cancel_appointment_by_client(appointment_id, user["id"], user["role"])
    for message in messages:
        flash(message, "success" if success else "error")
    return redirect("/appointments")
