from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from pony import orm
from pony.flask import Pony

from app import config


# Flask application
app = Flask(__name__)
app.config.from_object(config.Config)

# Pony orm
db = orm.Database()
db.bind(**app.config["PONY"])

# Flask login
login_manager = LoginManager()
login_manager.init_app(app)

# Blueprints
from app.base.views import base
from app.auth.views import auth
app.register_blueprint(base)
app.register_blueprint(auth)


db.generate_mapping(create_tables=True)
Pony(app)