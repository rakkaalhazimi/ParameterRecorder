import os
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jdlfjds7834kjfksdfhdsds'

    DATABASE_NAME = "index.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False