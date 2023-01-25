from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.base.views import base
from app.base import services



@base.route("/projects/<int:project_id>/records/create", methods=["GET", "POST"])
@login_required
def create_record(project_id: int):
    context = {
        "id": project_id
    }

    if request.method == "POST":
        project = services.get_project_by_id(id=project_id)
        record_name = request.form["name"]

        if record_name.strip():
            record = services.add_record(name=record_name, project=project)
            
            for key, value in zip(
                request.form.getlist("parameter_key"),
                request.form.getlist("parameter_value")
            ):
                services.add_parameter(key=key, value=value, record=record)


            for key, value in zip(
                request.form.getlist("result_key"),
                request.form.getlist("result_value")
            ):
                services.add_result(key=key, value=value, record=record)

            flash("Record created")
            return redirect(url_for("base.home"))
        
        flash("failed to create record")

    return render_template("record_create.html", context=context)


@base.route("/records/<int:record_id>", methods=["GET", "POST"])
@login_required
def view_record(record_id: int):
    project = services.get_project_by_id(id=record_id)
    records = services.get_records_by_project(record_id=record_id)
    context = {
        "id":record_id, 
        "name": project.name,
        "records": records
    }

    return render_template("record_view.html", context=context)


@base.route("/records/update/<int:record_id>", methods=["GET", "POST"])
@login_required
def update_record(record_id: int):
    project = services.get_project_by_id(id=record_id)
    context = {
        "id":record_id, 
        "name": project.name
    }

    if request.method == "POST":
        project_name = request.form["name"]

        if project_name.strip():
            services.set_project(project, name=project_name)
            flash("Project updated")
            return redirect(url_for("base.home"))
        
        flash("failed to update project")
    
    return render_template("record_update.html", context=context)


@base.route("/records/delete/<int:record_id>", methods=["GET", "POST"])
@login_required
def delete_record(record_id: int):
    if request.method == "POST":
        services.remove_project(id=record_id)
        return redirect(url_for("base.home"))

    project = services.get_project_by_id(id=record_id)
    context = {
        "id":record_id,
        "name": project.name,
    }

    return render_template("record_delete.html", context=context)