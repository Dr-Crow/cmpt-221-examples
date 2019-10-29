from flask import render_template, session, redirect, url_for, flash
from .. import db
from ..models import User
from . import main
from .forms import ContactForm


# Our route for displaying the bootstrap template
@main.route('/', methods=['GET'])
def index():
    return render_template("index.html", pages=["Portfolio", "About", "Contact"]), 200
