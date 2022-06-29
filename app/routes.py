import os, sys
import platform
import datetime as dt
from flask import (
    render_template,
    send_file,
    url_for,
    redirect,
    request,
    make_response,
    abort,
    jsonify,
    session,
    flash)
from app import app
from app.models import *

# Home route
@app.route("/")
def index():
    return render_template("index.html", title="")

# Platform os
@app.route("/platform")
def get_platform_name():
    return platform.system()

# Environment type
@app.route("/env")
def get_env():
    return app.config["ENV"]
