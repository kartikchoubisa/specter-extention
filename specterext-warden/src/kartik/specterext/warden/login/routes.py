from flask import render_template
from ..service import WardenService




login_endpoint = WardenService.blueprint



@login_endpoint.route("/login", methods=["GET", "POST"])
def login():
    return "loginpage"
