from flask import render_template
from flask_login import login_required

from app.base.views import base
from app.base import services


@base.route("/")
@login_required
def home():
    projects = services.get_all_projects()
    return render_template("index.html", projects=projects)