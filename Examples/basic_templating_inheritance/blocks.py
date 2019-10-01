from flask import Flask, render_template

# Declare the Flask Object
app = Flask(__name__)


# Adding dynamic route with templates
@app.route("/template/<name>")
def template(name):
    return render_template("template.html", name=name), 200


# Adding route for root
@app.route("/")
def control():
    return render_template("control.html", name_of_page="Testing!", number_list=[1, 2, 3, 4, 5]), 200


# Run Flask Programmatically
if __name__ == "__main__":
    # Set Debug to true, set host IP to localhost, and set port to 80
    app.run(debug=True, host="127.0.0.1", port=80)

