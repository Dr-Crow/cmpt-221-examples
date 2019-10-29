from . import db


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
