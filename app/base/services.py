from pony import orm

from .models import Projects


def get_all_projects():
    return orm.select(project for project in Projects)

def get_project_by_id(id: int):
    return Projects.get(id=id)

def add_project(current_user, name):
    Projects(name=name, user=current_user)
    orm.commit()
    return True