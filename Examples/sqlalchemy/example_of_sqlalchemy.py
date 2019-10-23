from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask App
app = Flask(__name__)

# Configure Database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@127.0.0.1:5432/Test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Make the db object
db = SQLAlchemy(app)


# Describing the Role Table
class Role(db.Model):
    # Overriding the default name "Role" with roles
    __tablename__ = 'roles'

    # Describing the columns
    role_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    role_name = db.Column(db.Text, nullable=False)

    # Back Reference to User Model
    users = db.relationship('User', backref='role', lazy='dynamic')

    # How it should look if we call print
    def __repr__(self):
        return '<Role %r>' % self.role_name


# Describing the User Table
class User(db.Model):
    # Overriding the default name "User" with users
    __tablename__ = 'users'

    # Describing the columns
    user_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=True)

    # Foreign Key linking the Role Table
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))

    # How it should look if we call print
    def __repr__(self):
        return '<User %r>' % self.first_name


# print(Role.query.all())
# print(User.query.all())
#
# users_1 = User.query.filter_by(role_id=1).all()
# print(users_1[0].email)


@app.route('/<last_name>', methods=['GET'])
def index(last_name):
    # Query Database for information
    user = User.query.filter_by(last_name=last_name).first()
    if user is None:
        return "<p>The user you looked up can not be found!</p>"
    else:
        return "<p>First Name: {first_name} Last Name: {last_name} Email: {email}</p>".format(first_name=user.first_name,
                                                                                              last_name=user.last_name,
                                                                                              email=user.email)


# Run Flask Programmatically
if __name__ == "__main__":
    # Set Debug to true, set host IP to localhost, and set port to 80
    app.run(debug=True, host="127.0.0.1", port=80)
