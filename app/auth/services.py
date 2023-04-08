from pony import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User


def validate_registration(email, password, confirm_password):
    if password != confirm_password:
        return False

    email_is_exists = User.get(email=email)
    if email_is_exists:
        return False

    return True

def check_user_password(pwhash: str, password: str):
    return check_password_hash(pwhash, password)

def hash_user_password(password: str):
    return generate_password_hash(password)

@orm.db_session
def add_user(email, password):
    pwhash = hash_user_password(password)
    user = User(email=email, password=pwhash)
    orm.commit()
    return True

@orm.db_session
def find_user(email):
    return User.get(email=email)

