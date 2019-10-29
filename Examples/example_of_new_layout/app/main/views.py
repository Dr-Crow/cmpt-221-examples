from flask import render_template, redirect, flash
from .. import db
from ..models import User
from . import main
from .forms import ContactForm


# Allows us to declare our views outside the global scope.
# Declare our route to query last names
@main.route('/<last_name>', methods=['GET'])
def last_query(last_name):
    # Query Database for information
    user = User.query.filter_by(last_name=last_name).first()
    if user is None:
        return "<p>The user you looked up can not be found!</p>", 200
    else:
        return "<p>First Name: {first_name} Last Name: {last_name} Email: {email}</p>".format(first_name=user.first_name,
                                                                                              last_name=user.last_name,
                                                                                              email=user.email), 200


# Our route for displaying the bootstrap template
@main.route('/', methods=['GET'])
def index():
    return render_template("index.html", pages=["Portfolio", "About", "Contact"]), 200


# Adding route for root
@main.route("/form", methods=["GET", "POST"])
def form_view():
    # Initialize the form
    form = ContactForm()

    # Checks if the form has been submitted
    if form.validate_on_submit():
        print("here")
        # Creates pop with values
        flash("Form submitted: Name {}, Email {}, Phone {}, Message {}".format(form.name.data, form.email.data, form.phone_number.data, form.message.data))

        # Redirects the page back to the route
        return redirect("/form")
    return render_template("contact.html", form=form)
