import os
from pathlib import Path

from pytz import timezone

base_dir = Path(__file__).resolve().parent.parent

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jdlfjds7834kjfksdfhdsds'

    PONY = {
        'provider': 'sqlite',
        'filename': 'index.db',
        'create_db': True
    }

    TIMEZONE = timezone("Asia/Jakarta")
