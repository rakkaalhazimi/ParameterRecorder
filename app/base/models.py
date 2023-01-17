from pony import orm

from app import db


class Projects(db.Entity):
    name = orm.Required(str, max_len=255)
    records = orm.Set("Records")


class Records(db.Entity):
    name = orm.Required(str, max_len=255)
    project = orm.Required(Projects)
    parameters = orm.Set("Parameters")
    results = orm.Set("Results")


class Parameters(db.Entity):
    key = orm.Required(str)
    value = orm.Required(str)
    record = orm.Required(Records)


class Results(db.Entity):
    key = orm.Required(str)
    value = orm.Required(str)
    record = orm.Required(Records)

