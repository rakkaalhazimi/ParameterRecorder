from pony import orm

from .models import Projects, Records


def get_all_projects():
    return orm.select(project for project in Projects)

def get_project_by_id(id: int):
    return Projects.get(id=id)

def add_project(current_user: int, name: str):
    Projects(name=name, user=current_user)
    orm.commit()

def set_project(project: Projects, **attributes):
    project.set(**attributes)
    orm.commit()

def remove_project(id: int):
    Projects.get(id=id).delete()
    orm.commit()


def get_records_by_project(project_id: str):
    return Records.select(lambda record: record.project.id == project_id)