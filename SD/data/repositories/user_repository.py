from utils.db_helper import get_connection

def find_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    return row

def username_exists(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    return row is not None

def email_exists(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    return row is not None

def create_user(full_name, username, email, password, role):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (full_name, username, email, password, role) VALUES (?, ?, ?, ?, ?)",
        (full_name, username, email, password, role)
    )
    conn.commit()
    conn.close()
