# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
#   Desc.:      The business logic for the auth module
#   Purpose:    Controlling the server side behaviour of the pages
#   Author:     Joel Tannas
#   Date:       MAR 03, 2017
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Generic Imports: 
# ---------------------------------------------------------------------------

# Import the environ to retrieve the reCaptcha public key
from os import environ

# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
                  
# Import flask login
from flask_login import login_user, logout_user, login_required, \
                        current_user

# Import tools for working with urls
from urllib.parse import urlparse, urljoin

# ---------------------------------------------------------------------------
# App Imports: 
# ---------------------------------------------------------------------------
# Import the database object & login_manager
from .. import db

# ---------------------------------------------------------------------------
# Module_Auth Imports: 
# ---------------------------------------------------------------------------
# Import the login manager
from . import login_manager

# Import module forms
from .forms import LoginForm, RegistrationForm

# Import module models
from .models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# ---------------------------------------------------------------------------
# Methods & Decorators: 
# ---------------------------------------------------------------------------

def is_safe_url(target):
    """ Check to see if a URL redirects within the website"""
    # by http://flask.pocoo.org/snippets/62/
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


# flask_login required decorator and method 
@login_manager.user_loader
def load_user(user_id):
    """ Gets the user for a given user id"""
    return User.query.get(user_id)

# ---------------------------------------------------------------------------
# Sign In Route: 
# ---------------------------------------------------------------------------


@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    """Sign-In page for the user"""

    # Load the WTForm object
    form = LoginForm(request.form)

    # If sign in form is submitted, verify the sign in form
    if form.validate_on_submit():

        # Query the user by email
        user = User.query.filter_by(email=form.email.data).first()

        # Password verification (sqlalchemy deals with the hashes)
        if user and user.password == form.password.data:

            # Login & notify
            login_user(user)
            flash('Welcome %s' % user.name, 'info')
            
            # Send the user on their way
            next = request.args.get('next')
            if not is_safe_url(next):
                return abort(400)
            return redirect(next or url_for('auth.signin'))

        flash('Wrong email or password', 'error')
    
    return render_template("auth/signin.html", form=form)

# ---------------------------------------------------------------------------
# Sign Up Route: 
# ---------------------------------------------------------------------------
@mod_auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    
    # Load the WTForm
    form = RegistrationForm(request.form)
    
    # If sign up form is submitted via POST, validate the form
    if form.validate_on_submit():
        
        # Create the user and create a database entry
        user = User(form.name.data, form.email.data, form.password.data, 0, 0)
                    
        db.session.add(user)
        db.session.commit()
        
        flash('Thanks for registering', 'info')
        
        return redirect(url_for('auth.signin'))
    
    else:    
        return render_template('auth/signup.html', form=form, 
            RECAPTCHA_PUB_KEY=environ.get("RECAPTCHA_PUB_KEY"))

# ---------------------------------------------------------------------------
# Sign Out Route: 
# ---------------------------------------------------------------------------            
@mod_auth.route("/signout/")

def signout():

    if current_user.is_authenticated:
        logout_user()
        flash("You have been logged out", 'info')
        
    return redirect(url_for("auth.signin"))