import os
from app import create_app

# Creates an app using our function create_app. Also passes in default for config is nothing is set
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# Run Flask Programmatically
if __name__ == "__main__":
    # Set Debug to true, set host IP to localhost, and set port to 80
    app.run(debug=True, host="127.0.0.1", port=80)
