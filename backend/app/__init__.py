from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

#load_dotenv()
db = SQLAlchemy()
migrate = Migrate()

# Singleton for the App instance, for using in other code
app = ''


def create_app(ConfigClass):

    app = Flask(__name__)
    app.config.from_object(ConfigClass)
    #TODO: General cors acces in place, do we want to lock this down fruther? 
    CORS(app)
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    with app.app_context():
        # Dunno about this.. but it is here from other projects
        return app
