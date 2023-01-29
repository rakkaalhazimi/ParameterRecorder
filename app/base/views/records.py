from itertools import zip_longest

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
                if services.validate_parameter_or_result(key, value):
                    services.add_parameter(key=key, value=value, record=record)


            for key, value in zip(
                request.form.getlist("result_key"),
                request.form.getlist("result_value")
            ):
                if services.validate_parameter_or_result(key, value):
                    services.add_result(key=key, value=value, record=record)

            flash("Record created")
            return redirect(url_for("base.view_project", project_id=project_id))
        
        flash("failed to create record")

    return render_template("record_create.html", context=context)


@base.route("/projects/<int:project_id>/records/<int:record_id>", methods=["GET", "POST"])
@login_required
def view_record(project_id: int, record_id: int):
    record = services.get_record_by_id(record_id=record_id)
    parameters = services.get_parameters_by_record(record_id=record_id)
    results = services.get_results_by_record(record_id=record_id)

    context = {
        "id":record_id, 
        "name": record.name,
        "parameters": parameters,
        "results": results
    }

    return render_template("record_view.html", context=context)


@base.route("/projects/<int:project_id>/records/update/<int:record_id>", methods=["GET", "POST"])
@login_required
def update_record(project_id: int, record_id: int):
    record = services.get_record_by_id(record_id=record_id)
    parameters = services.get_parameters_by_record(record_id=record_id)
    results = services.get_results_by_record(record_id=record_id)

    context = {
        "project_id": project_id,
        "record_id": record_id,
        "name": record.name,
        "parameters": parameters,
        "results": results
    }

    if request.method == "POST":
        record_name = request.form["name"]

        if record.name != record_name and record_name.strip():
            services.set_record(record, name=record_name)

        for key, value, id_ in zip_longest(
            request.form.getlist("parameter_key"),
            request.form.getlist("parameter_value"),
            request.form.getlist("parameter_id"),
        ):
            print("Id: ", id_)
            if id_:
                parameter = services.get_parameter_by_id(id_)
                services.set_parameter(parameter=parameter, key=key, value=value)
            
            elif services.validate_parameter_or_result(key, value):
                services.add_parameter(key, value, record)


        for key, value, id_ in zip_longest(
            request.form.getlist("result_key"),
            request.form.getlist("result_value"),
            request.form.getlist("result_id")
        ):
            if id_:
                result = services.get_result_by_id(id_)
                services.set_result(result, key=key, value=value)
            
            elif services.validate_parameter_or_result(key, value):
                services.add_result(key, value, record)

        flash("Record updated")
        return redirect(url_for("base.view_project", project_id=project_id))
        
    flash("failed to update project")
    
    return render_template("record_update.html", context=context)


@base.route("/projects/<int:project_id>/records/delete/<int:record_id>", methods=["GET", "POST"])
@login_required
def delete_record(project_id: int, record_id: int):
    if request.method == "POST":
        services.remove_record(id=record_id)
        return redirect(url_for("base.view_project", project_id=project_id))

    record = services.get_record_by_id(record_id=record_id)
    context = {
        "project_id": project_id,
        "record_id": record_id,
        "name": record.name,
    }

    return render_template("record_delete.html", context=context)