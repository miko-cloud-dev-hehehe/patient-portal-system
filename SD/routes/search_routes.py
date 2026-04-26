from flask import Blueprint, render_template, request, session, redirect
from application.search.query_processing import smart_search

search_bp = Blueprint("search", __name__)

@search_bp.route("/search")
def search():
    if "user" not in session:
        return redirect("/")
    if session["user"]["role"] == "admin":
        return render_template("search.html", results=[], q="", user=session["user"])
    query = request.args.get("q", "")
    results = smart_search(query, session["user"]["id"])
    return render_template("search.html", results=results, q=query, user=session["user"])
