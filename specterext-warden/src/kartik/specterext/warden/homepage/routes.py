from flask import render_template
from ..service import WardenService




homepage_endpoint = WardenService.blueprint



@homepage_endpoint.route("/home", methods=["GET", "POST"])
def homepage():
    return "homepage"
