from flask import Blueprint


base = Blueprint("base", __name__)


from . import home, projects, records