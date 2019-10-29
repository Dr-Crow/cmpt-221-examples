import os
from app import create_app, db
from app.models import User, Role

# Creates an app using our function create_app. Also passes in default for config is nothing is set
app = create_app(os.getenv('FLASK_CONFIG') or 'default')


# Allows us to run Flask via Flask Shell. Make sure to export/set FLASK_APP="flask_run.py"
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


# Run Flask Programmatically
if __name__ == "__main__":
    # Set Debug to true, set host IP to localhost, and set port to 80
    app.run(debug=True, host="127.0.0.1", port=80)
