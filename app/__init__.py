from flask import Flask
from flask_login import LoginManager
from pony import orm
from pony.flask import Pony

from app.config import Config


# Extension
db = orm.Database()
login_manager = LoginManager()


def clear_database():
    db.drop_all_tables()
    db.create_tables()

def create_app(config: object = Config):
    # Flask application
    app = Flask(__name__)
    app.config.from_object(config)
    Pony(app)

    # Blueprints
    from app.base.views import base
    from app.auth.views import auth
    app.register_blueprint(base)
    app.register_blueprint(auth)

    # Pony orm
    if not db.provider_name:
        db.bind(**app.config["PONY"])
        db.generate_mapping(create_tables=True)

    # Flask login
    login_manager.init_app(app)

    return app
