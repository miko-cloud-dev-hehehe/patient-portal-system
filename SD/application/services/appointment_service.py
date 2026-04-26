from data.repositories.appointment_repository import save_appointment, fetch_user_appointments, fetch_all_appointments_with_users, get_appointment_by_id, update_appointment_status
from data.repositories.record_repository import create_record_for_completed_appointment
from utils.validators import validate_appointment_form, validate_record_form

def create_appointment(form_data, user_id):
    errors = validate_appointment_form(form_data)
    if errors:
        return False, errors
    save_appointment(
        user_id=user_id,
        name=form_data.get("name", "").strip(),
        appointment_date=form_data.get("date", "").strip(),
        schedule=form_data.get("schedule", "").strip(),
        notes=form_data.get("notes", "").strip()
    )
    return True, ["Appointment added successfully."]

def get_user_appointments(user_id):
    return fetch_user_appointments(user_id)

def get_all_appointments_for_admin():
    return fetch_all_appointments_with_users()

def complete_appointment_by_admin(appointment_id, admin_role, form_data):
    if admin_role != "admin":
        return False, ["Only the admin can mark an appointment as done."]
    appointment = get_appointment_by_id(appointment_id)
    if not appointment:
        return False, ["Appointment not found."]
    if appointment["status"] == "Cancelled":
        return False, ["Cancelled appointments cannot be marked as done."]
    if appointment["status"] == "Done":
        return False, ["Appointment is already marked as done."]
    errors = validate_record_form(form_data)
    if errors:
        return False, errors
    update_appointment_status(appointment_id, "Done")
    create_record_for_completed_appointment(
        appointment,
        form_data.get("test_name", "").strip(),
        form_data.get("value", "").strip(),
        form_data.get("status", "").strip(),
        form_data.get("plain_explanation", "").strip()
    )
    return True, ["Appointment marked as done and record saved."]

def cancel_appointment_by_client(appointment_id, user_id, role):
    appointment = get_appointment_by_id(appointment_id)
    if not appointment:
        return False, ["Appointment not found."]
    if role == "admin":
        return False, ["Admin cannot cancel client appointments here."]
    if appointment["user_id"] != user_id:
        return False, ["You are not allowed to cancel this appointment."]
    if appointment["status"] == "Done":
        return False, ["Completed appointments cannot be cancelled."]
    if appointment["status"] == "Cancelled":
        return False, ["Appointment is already cancelled."]
    update_appointment_status(appointment_id, "Cancelled")
    return True, ["Appointment cancelled successfully."]
