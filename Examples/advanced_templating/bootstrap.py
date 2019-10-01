from flask import Flask, render_template

# Declare the Flask Object
app = Flask(__name__)

# Adding route for root
@app.route("/")
def root():
    return render_template("index.html", pages=["Portfolio", "About", "Contact"]), 200

# Adding route for about page
@app.route("/about")
def about():
    return render_template("about.html"), 200


# Run Flask Programmatically
if __name__ == "__main__":
    # Set Debug to true, set host IP to localhost, and set port to 80
    app.run(debug=True, host="127.0.0.1", port=80)

