from datetime import datetime


from flask_login import UserMixin
from pony import orm

from app import db


class User(db.Entity, UserMixin):
    email = orm.Required(str, unique=True)
    password = orm.Required(str)
    last_login = orm.Optional(datetime)
    is_admin = orm.Optional(bool, default=False)
    created_at = orm.Required(
        datetime, default=datetime.utcnow())
    projects = orm.Set("Projects")