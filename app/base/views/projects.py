from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from pony import orm

from app.base.views import base
from app.base import services



@base.route("/projects/create", methods=["GET", "POST"])
@login_required
def create_project():
    if request.method == "POST":
        project_name = request.form["name"]
        
        if project_name.strip():
            services.add_project(current_user=current_user, name=project_name)
            flash("Project created")
            return redirect(url_for("base.home"))
        
        flash("failed to create project")

    return render_template("project_create.html")


@base.route("/projects/<int:project_id>", methods=["GET", "POST"])
@login_required
def view_project(project_id: int):
    project = services.get_project_by_id(id=project_id)
    records = services.get_records_by_project(project_id=project_id)
    context = {
        "id":project_id, 
        "name": project.name,
        "records": records
    }

    return render_template("project_view.html", context=context)


@base.route("/projects/update/<int:project_id>", methods=["GET", "POST"])
@login_required
def update_project(project_id: int):
    project = services.get_project_by_id(id=project_id)
    context = {
        "id":project_id, 
        "name": project.name
    }

    if request.method == "POST":
        project_name = request.form["name"]

        if project_name.strip():
            services.set_project(project, name=project_name)
            flash("Project updated")
            return redirect(url_for("base.home"))
        
        flash("failed to update project")
    
    return render_template("project_update.html", context=context)


@base.route("/projects/delete/<int:project_id>", methods=["GET", "POST"])
@login_required
def delete_project(project_id: int):
    if request.method == "POST":
        services.remove_project(id=project_id)
        return redirect(url_for("base.home"))

    project = services.get_project_by_id(id=project_id)
    context = {
        "id":project_id,
        "name": project.name,
    }

    return render_template("project_delete.html", context=context)