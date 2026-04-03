from flask import Flask
from .models import db

def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=False)
    # minimal config; can be overridden by env vars
    app.config.setdefault("SQLALCHEMY_DATABASE_URI", "sqlite:///aceest_fitness.db")
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    if config_object:
        app.config.from_object(config_object)

    # db.init_app(app)

    # register blueprints
    from .routes.clients import bp as clients_bp
    app.register_blueprint(clients_bp, url_prefix="/clients")

    # simple health route
    @app.route("/health")
    def health():
        return {"status": "ok"}, 200

    return app
