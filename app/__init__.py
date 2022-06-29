import os
import platform
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config


app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)


# Import configuration profile based on FLASK_ENV variable - defaults to Production
if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object(config.DevelopmentConfig)
elif os.environ.get('FLASK_ENV') == 'testing':
    app.config.from_object(config.TestingConfig)
else:
    app.config.from_object(config.ProductionConfig)


# Select Environment Type (Production / Development)
OS_NAME = platform.system()

if OS_NAME == "Linux":
    app.config["ENV"] = "production"
else:
    app.config["ENV"] = "development"



# Import routes here
from app.routes import *