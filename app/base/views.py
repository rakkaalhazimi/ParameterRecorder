import flask
from flask_login import login_required


base = flask.Blueprint("base", __name__)


@base.route("/")
@login_required
def home():
    return "Hello world"