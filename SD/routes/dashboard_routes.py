from flask import Blueprint, render_template, session, redirect
from application.services.record_service import get_user_records
from application.services.appointment_service import get_user_appointments, get_all_appointments_for_admin

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    role = session["user"]["role"]
    user_id = session["user"]["id"]
    if role == "admin":
        appointments = get_all_appointments_for_admin()[:5]
        return render_template("dashboard.html", user=session["user"], records=[], appointments=appointments)
    records = [dict(r) for r in get_user_records(user_id)][:3]
    appointments = get_user_appointments(user_id)[:3]
    return render_template("dashboard.html", user=session["user"], records=records, appointments=appointments)
