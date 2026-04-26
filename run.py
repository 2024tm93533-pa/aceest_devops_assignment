import os
from app import create_app
from app.models import db

app = create_app()

# Root route (fix for "Not Found")
@app.route("/")
def home():
    return {"message": "ACEest Fitness API is running 🚀"}

# Helper to create DB tables quickly (for local dev)
@app.cli.command("init-db")
def init_db():
    """Initialize the database (create tables)."""
    with app.app_context():
        db.create_all()
        print("Database initialized.")

if __name__ == "__main__":
    # choose host & port for local dev
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.environ.get("FLASK_RUN_PORT", 8000))
    app.run(host=host, port=port, debug=True)