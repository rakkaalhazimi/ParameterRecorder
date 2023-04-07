from pony import orm

from .models import User


def validate_registration(email, password, confirm_password):

    if password != confirm_password:
        return False

    email_is_exists = User.get(email=email)
    if email_is_exists:
        return False


def add_user(email, password):
    User(email=email, password=password)
    orm.commit()
    return True