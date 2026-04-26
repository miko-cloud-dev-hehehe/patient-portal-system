from utils.db_helper import get_connection

def save_appointment(user_id, name, appointment_date, schedule, notes=""):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO appointments (user_id, name, appointment_date, schedule, notes, status) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, name, appointment_date, schedule, notes, "Pending")
    )
    conn.commit()
    conn.close()

def fetch_user_appointments(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments WHERE user_id = ? ORDER BY appointment_date ASC, id DESC", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def fetch_all_appointments_with_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT appointments.*, users.full_name, users.username
        FROM appointments
        JOIN users ON users.id = appointments.user_id
        ORDER BY appointment_date ASC, appointments.id DESC
        '''
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_appointment_by_id(appointment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments WHERE id = ?", (appointment_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def update_appointment_status(appointment_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE appointments SET status = ? WHERE id = ?", (status, appointment_id))
    conn.commit()
    conn.close()
