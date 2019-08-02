from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(ConfigClass):

    app = Flask(__name__)
    app.config.from_object(ConfigClass)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    with app.app_context():


        return app


from app.models import Boat, Crew  # noqa: E402
