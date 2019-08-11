from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()


def create_app(ConfigClass):

    app = Flask(__name__)
    app.config.from_object(ConfigClass)

    db.init_app(app)

    CORS(app)

    # DB: We aren't going to worry about this for now (testing direct SQL)
    # migrate.init_app(app, db)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    with app.app_context():
        return app
