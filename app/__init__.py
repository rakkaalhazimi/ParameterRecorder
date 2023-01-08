from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app import config



app = Flask(__name__)
app.config.from_object(config.Config)

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

login_manager = LoginManager()
login_manager.init_app(app)


from app.base.views import base
from app.auth.views import auth
app.register_blueprint(base)
app.register_blueprint(auth)


with app.app_context():
    db.create_all()