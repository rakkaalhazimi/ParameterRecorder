from pony import orm

from .models import Projects


def add_project(current_user, name):
    Projects(name=name, user=current_user)
    orm.commit()
    return True