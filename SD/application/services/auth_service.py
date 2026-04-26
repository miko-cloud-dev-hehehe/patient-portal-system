from data.repositories.user_repository import find_user_by_username, create_user, username_exists, email_exists
from utils.validators import validate_signup_form, validate_login_form

def login_user(form_data):
    errors = validate_login_form(form_data)
    if errors:
        return None, errors
    username = form_data.get("username", "").strip()
    password = form_data.get("password", "").strip()
    user = find_user_by_username(username)
    if not user:
        return None, ["Account not found."]
    if user["password"] != password:
        return None, ["Incorrect password."]
    return dict(user), []

def register_user(form_data):
    errors = validate_signup_form(form_data)
    username = form_data.get("username", "").strip()
    email = form_data.get("email", "").strip()
    if username_exists(username):
        errors.append("Username already exists.")
    if email_exists(email):
        errors.append("Email already exists.")
    if errors:
        return False, errors
    create_user(form_data.get("full_name", "").strip(), username, email, form_data.get("password", "").strip(), "client")
    return True, ["Account created successfully. Please log in."]
