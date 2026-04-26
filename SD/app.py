from flask import Flask
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.appointment_routes import appointment_bp
from routes.records_routes import records_bp
from routes.search_routes import search_bp

app = Flask(__name__, template_folder="presentation/templates", static_folder="presentation/static")
app.secret_key = "secret123"

for bp in [auth_bp, dashboard_bp, appointment_bp, records_bp, search_bp]:
    app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)
