from flask import render_template
from . import main
from flask_login import login_required


# Our route for displaying the bootstrap template
@main.route('/', methods=['GET'])
def index():
    return render_template("index.html", pages=["Portfolio", "About", "Contact"]), 200


@main.route('/secret', methods=['GET'])
@login_required
def secret():
    return "Only authenticated users can see this!", 200
