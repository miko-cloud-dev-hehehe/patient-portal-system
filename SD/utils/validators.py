import re
from datetime import datetime

def validate_signup_form(data):
    errors = []
    full_name = data.get("full_name", "").strip()
    username = data.get("username", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "").strip()
    confirm_password = data.get("confirm_password", "").strip()

    if len(full_name) < 3:
        errors.append("Full name must be at least 3 characters.")
    if len(username) < 3:
        errors.append("Username must be at least 3 characters.")
    if " " in username:
        errors.append("Username must not contain spaces.")
    if "@" not in email or "." not in email:
        errors.append("Enter a valid email address.")
    if len(password) < 8:
        errors.append("Password must be at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        errors.append("Password must include at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        errors.append("Password must include at least one number.")
    if not re.search(r"[^A-Za-z0-9]", password):
        errors.append("Password must include at least one special character.")
    if password != confirm_password:
        errors.append("Passwords do not match.")
    return errors

def validate_login_form(data):
    errors = []
    if not data.get("username", "").strip():
        errors.append("Username is required.")
    if not data.get("password", "").strip():
        errors.append("Password is required.")
    return errors

def validate_appointment_form(data):
    errors = []
    name = data.get("name", "").strip()
    appointment_date = data.get("date", "").strip()
    schedule = data.get("schedule", "").strip()

    if len(name) < 3:
        errors.append("Appointment name must be at least 3 characters.")
    if schedule not in ["Morning", "Afternoon"]:
        errors.append("Please choose morning or afternoon.")

    if not appointment_date:
        errors.append("Appointment date is required.")
    else:
        try:
            chosen = datetime.strptime(appointment_date, "%Y-%m-%d").date()
            if chosen < datetime.today().date():
                errors.append("Appointment date cannot be in the past.")
        except ValueError:
            errors.append("Enter a valid appointment date.")
    return errors

def validate_record_form(data):
    errors = []
    if len(data.get("test_name", "").strip()) < 2:
        errors.append("Test name is required.")
    if len(data.get("value", "").strip()) < 1:
        errors.append("Result value is required.")
    if data.get("status", "").strip() not in ["Normal", "Borderline", "High"]:
        errors.append("Please choose a valid result status.")
    if len(data.get("plain_explanation", "").strip()) < 5:
        errors.append("Explanation must be at least 5 characters.")
    return errors
