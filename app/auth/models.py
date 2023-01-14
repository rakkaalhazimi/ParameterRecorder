from datetime import datetime

from flask_login import UserMixin
from pony import orm

from app import db


class User(db.Entity, UserMixin):
    email = orm.Required(str, unique=True)
    password = orm.Required(str)
    last_login = orm.Optional(datetime)