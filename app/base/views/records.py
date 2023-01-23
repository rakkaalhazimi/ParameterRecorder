from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.base.views import base
from app.base import services



@base.route("/records/create", methods=["GET", "POST"])
@login_required
def create_record():
    if request.method == "POST":
        record_name = request.form["name"]
        # parameters = request.form["parameter_key"]
        # results = request.form["result_key"]

        # print(record_name, parameters, results)
        print(request.form.keys())
        
        # if record_name.strip():
        #     services.add_project(current_user=current_user, name=record_name)
        #     flash("Record created")
        #     return redirect(url_for("base.home"))
        
        # flash("failed to create record")

    return render_template("record_create.html")


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