from utils.db_helper import get_connection

def fetch_user_records(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records WHERE user_id = ? ORDER BY id DESC", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def create_record_for_completed_appointment(appointment, test_name, value, status, explanation):
    existing = _find_record_by_appointment_id(appointment["id"])
    if existing:
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO records (user_id, appointment_id, test_name, value, status, plain_explanation) VALUES (?, ?, ?, ?, ?, ?)",
        (appointment["user_id"], appointment["id"], test_name, value, status, explanation)
    )
    conn.commit()
    conn.close()

def _find_record_by_appointment_id(appointment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM records WHERE appointment_id = ?", (appointment_id,))
    row = cursor.fetchone()
    conn.close()
    return row
