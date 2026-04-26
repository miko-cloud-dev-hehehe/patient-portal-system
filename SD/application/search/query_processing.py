from data.repositories.record_repository import fetch_user_records

SEARCH_KEYWORDS = {
    "heart": ["Heart Rate", "Blood Pressure"],
    "heart rate": ["Heart Rate"],
    "bp": ["Blood Pressure"],
    "blood pressure": ["Blood Pressure"],
    "sugar": ["Blood Sugar"],
    "sugar level": ["Blood Sugar"],
    "glucose": ["Blood Sugar"],
    "cholesterol": ["Cholesterol"],
    "cbc": ["Complete Blood Count"],
    "blood test": ["Complete Blood Count", "Hemoglobin"],
    "hemoglobin": ["Hemoglobin"],
    "pulse": ["Heart Rate"]
}

def smart_search(query, user_id):
    query = (query or "").strip().lower()
    if not query:
        return []
    records = fetch_user_records(user_id)
    mapped_terms = SEARCH_KEYWORDS.get(query, [query])
    results = []
    for row in records:
        haystack = " ".join([str(row["test_name"]), str(row["value"]), str(row["status"]), str(row["plain_explanation"])]).lower()
        if any(term.lower() in haystack for term in mapped_terms):
            results.append(dict(row))
    return results
