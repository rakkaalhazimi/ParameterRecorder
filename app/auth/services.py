import re

from pony import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User


def validate_email(email: str) -> bool:
    address = re.compile(
    r"""
    \b
    [\w\d.+\-_]+            # Username
    @                       # (add symbol)
    ([\w\d.]+\.)+           # Domain name prefix
    (com|edu|org|co./id)    # Top-level domains
    \b
    """,
    re.VERBOSE)

    found = address.match(email)
    if found:
        return True
    else:
        return False

def validate_registration(email, password, confirm_password):
    if password != confirm_password:
        return False

    email_is_valid = validate_email(email)
    if not email_is_valid:
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

