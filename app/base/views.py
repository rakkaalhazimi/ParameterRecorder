import flask


base = flask.Blueprint("base", __name__)


@base.route("/")
def home():
    return "Hello world"