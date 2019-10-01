from flask import Flask

# Create the app object, which is the "Flask server"
app = Flask(__name__)


# Create a static route that displays simple HTML. You are about to browser to it via index or /
@app.route("/index")
@app.route("/")
def index():
    return "<h1>Hello this is a static route</h1>"


# Create a dynamic route
@app.route("/input/<thing>")
def input(thing):
    return "<h1>Hell this is a dynamic route. Thing: " + thing + " </h1>"


# Created an "advanced" HTML Page
@app.route("/html")
def html():
    return """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>
"""


# Allows you to run the flask server like a normal python file
if __name__ == "__main__":
    app.run()
