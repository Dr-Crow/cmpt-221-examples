from flask import Flask, render_template, flash, redirect
from forms import ContactForm


# Declare the Flask Object
app = Flask(__name__)

# Create secret key
app.config["SECRET_KEY"] = "2328324742304902112908-23"


# Adding route for root
@app.route("/", methods=["GET", "POST"])
def root():
    # Initialize the form
    form = ContactForm()

    # Checks if the form has been submitted
    if form.validate_on_submit():
        print("here")
        # Creates pop with values
        flash("Form submitted: Name {}, Email {}, Phone {}, Message {}".format(form.name.data, form.email.data, form.phone_number.data, form.message.data))

        # Redirects the page back to the route
        #return redirect("/")
    return render_template("contact.html", form=form)


# Run Flask Programmatically
if __name__ == "__main__":
    # Set Debug to true, set host IP to localhost, and set port to 80
    app.run(debug=True, host="127.0.0.1", port=80)

