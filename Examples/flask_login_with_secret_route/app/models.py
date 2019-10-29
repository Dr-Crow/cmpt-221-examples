from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager


# Spot for all our models
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
# Added UserMixin to add needed fields for Flask Login
class User(UserMixin, db.Model):
    # Overriding the default name "User" with users
    __tablename__ = 'users'

    # Describing the columns
    user_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False)

    # Not storing Password in plain text storing hash now!
    password_hash = db.Column(db.Text, nullable=False)

    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=True)

    # Foreign Key linking the Role Table
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))

    # When the attribute password is called we will return the following thanks to @property
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    # When we set the password, this function will happen automatically
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # Add a function to verify hashing is working correctly
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Override for default get_id
    def get_id(self):
        return self.user_id

    # How it should look if we call print
    def __repr__(self):
        return '<User %r>' % self.email


# Registering the user_loader function with Flask-login to get information about
# user id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
