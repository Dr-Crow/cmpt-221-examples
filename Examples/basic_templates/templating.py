from flask import Flask, render_template

# Declare the Flask Object
app = Flask(__name__)


# Adding dynamic route name
@app.route("/name/<name>")
def basic(name):
    # Return the snip-it of HTML and status code 200
    return "<h1> Hello, " + name + "! </h1>", 200


# Adding dynamic route with templates
@app.route("/template/<name>")
def template(name):
    return render_template("name.html", name=name), 200


# Run Flask Programmatically
if __name__ == "__main__":
    # Set Debug to true, set host IP to localhost, and set port to 80
    app.run(debug=True, host="127.0.0.1", port=80)

