from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from pony import orm

from app.base import models, services


base = Blueprint("base", __name__)


@base.route("/")
@login_required
def home():
    projects = orm.select(project.name for project in models.Projects)
    return render_template("index.html", projects=projects)


@base.route("/projects/create", methods=["GET", "POST"])
def create_project():
    if request.method == "POST":
        project_name = request.form["name"]
        
        if project_name.strip():
            models.Projects(name=project_name)
            orm.commit()
            flash("Project created")
            return redirect(url_for("base.home"))
        
        flash("failed to create project")

    return render_template("project_create.html")


@base.route("/projects/update/<int:project_id>", methods=["GET", "POST"])
def update_project(project_id: int):
    project = models.Projects.get(id=project_id)
    context = {
        "id":project_id, 
        "name": project.name
    }

    if request.method == "POST":
        project_name = request.form["name"]

        if project_name.strip():
            project.name = project_name
            orm.commit()
            flash("Project updated")
            return redirect(url_for("base.home"))
        
        flash("failed to update project")
    
    return render_template("project_update.html", context=context)