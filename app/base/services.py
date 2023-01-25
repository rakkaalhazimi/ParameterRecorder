from typing import Iterable

from pony import orm

from .models import Projects, Records, Parameters, Results


# Projects
def get_all_projects() -> Iterable:
    return orm.select(project for project in Projects)

def get_project_by_id(id: int):
    return Projects.get(id=id)

def add_project(current_user: int, name: str) -> Projects:
    project = Projects(name=name, user=current_user)
    orm.commit()
    return project

def set_project(project: Projects, **attributes):
    project.set(**attributes)
    orm.commit()

def remove_project(id: int):
    Projects.get(id=id).delete()
    orm.commit()


# Records
def add_record(name: str, project: Projects) -> Records:
    record = Records(name=name, project=project)
    orm.commit()
    return record

def get_records_by_project(project_id: int) -> Iterable:
    return Records.select(lambda record: record.project.id == project_id)

def get_record_by_id(record_id: int) -> Records:
    return Records.get(id=record_id)


# Parameters
def add_parameter(key: str, value: str, record: Records) -> Parameters:
    parameter = Parameters(key=key, value=value, record=record)
    orm.commit()
    return parameter

def get_parameters_by_record(record_id: int) -> Iterable:
    return Parameters.select(lambda parameter: parameter.record.id == record_id)


# Results
def add_result(key: str, value: str, record: Records) -> Parameters:
    result = Results(key=key, value=value, record=record)
    orm.commit()
    return result

def get_results_by_record(record_id: int) -> Iterable:
    return Results.select(lambda result: result.record.id == record_id)