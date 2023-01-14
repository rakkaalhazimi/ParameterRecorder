from pony import orm

from .models import User


def validate_registration(email, password, confirm_password):

    if password != confirm_password:
        return False

    try:
        User(email=email, password=password)
        orm.commit()
        return True

    except orm.TransactionIntegrityError as e:
        print(e)
        return False
