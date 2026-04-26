from data.repositories.record_repository import fetch_user_records

def get_user_records(user_id):
    return fetch_user_records(user_id)
