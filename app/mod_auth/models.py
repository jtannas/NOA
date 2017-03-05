# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
#   Desc.:      Database models for the auth module
#   Purpose:    Defines the user tables
#   Author:     Joel Tannas
#   Date:       MAR 03, 2017
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Imports:
# ---------------------------------------------------------------------------
# Import the database & base table design from the main application module
from app import db, Base

# Import UserMixin from flask_login to extend the User table
from flask_login import UserMixin

# Import password / encryption helper tools
from sqlalchemy_utils import PasswordType

# Import wtforms validators to embed into the model for use with WTForms_Alchemy
from wtforms.validators import Email, Regexp


# ---------------------------------------------------------------------------
# User Model
# ---------------------------------------------------------------------------
class User(Base, UserMixin):
    """ SQLAlchemy User table definition """

    # ------------------
    # Data Structure
    # ------------------
    __tablename__ = 'auth_user'

    name    = db.Column(db.String(128),  nullable=False)
    email    = db.Column(db.String(128), 
        nullable=False,
        unique=True,
        info={'validators': Email()})
    # Password: 8+ chars, uppercase, lowercase, and numerical    
    password = db.Column(PasswordType(schemes=['argon2']), 
        nullable=False,
        info={'validators': Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', 
                                message='Does not conform to password requirements')})
    role     = db.Column(db.SmallInteger, nullable=False)
    status   = db.Column(db.SmallInteger, nullable=False)

    # ------------------
    # Methods
    # ------------------
    def __init__(self, name, email, password, role=0, status=0):
        """ New User creation procedure """

        self.name     = name
        self.email    = email
        self.password = password
        self.role     = role
        self.status   = status

    def __repr__(self):
        """ Return Printable representation of the object """
        return '<User %r>' % (self.name)