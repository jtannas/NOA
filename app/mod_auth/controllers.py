''' The business logic & routing controller of this module

The is the controller aspect of the module.

References:
    - The Parent Application
    - The Parent Application database
    - The Parent Application utilities
    - This module's: database models, jinja templates, and WTForms

Yields:
    - Method: Load User Record
    - Route: User Sign-In
    - Route: New User Registration
    - Route: User Log-out
    
Todo:
    - Overhaul expected in the near future - See the GitHub Projects
'''

# ---------------------------------------------------------------------------
# Generic Imports: 
# ---------------------------------------------------------------------------
from os import environ
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from flask_login import login_user, logout_user, login_required, \
                        current_user

# ---------------------------------------------------------------------------
# Application Imports: 
# ---------------------------------------------------------------------------
from .. import db
from ..utils import is_safe_url

from . import login_manager
from .forms import LoginForm, RegistrationForm
from .models import User

# ---------------------------------------------------------------------------
# Methods, Decorators, and Vars: 
# ---------------------------------------------------------------------------

# Define the blueprint for import into the parent application
mod_auth = Blueprint('auth', __name__, url_prefix='/auth',
                    template_folder='templates',
                    static_folder='static')
                    
# flask_login required decorator and method 
@login_manager.user_loader
def load_user(user_id: int):
    ''' Gets the user for a given user id'''
    
    return User.query.get(user_id)

# ---------------------------------------------------------------------------
# Sign In Route: 
# ---------------------------------------------------------------------------
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    '''Sign-In page for the user'''

    # Load the WTForm object
    form = LoginForm(request.form)

    # If sign in form is submitted, verify the sign in form
    if form.validate_on_submit():

        # Query the user by email
        user = User.query.filter_by(email=form.email.data).first()

        # Password verification (sqlalchemy deals with the hashes)
        if user and user.password == form.password.data:

            if current_user.is_authenticated:
                logout_user()

            # Login & notify
            login_user(user)
            flash('Welcome %s' % user.name, 'info')
            
            # Send the user on their way
            next = request.args.get('next')
            if not is_safe_url(next):
                return abort(400)
            return redirect(next or url_for('base.index'))

        flash('Wrong email or password', 'error')
    
    return render_template("./signin.html", form=form)

# ---------------------------------------------------------------------------
# Sign Up Route: 
# ---------------------------------------------------------------------------
@mod_auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    ''' Registration page for new users '''
    
    # Load the user form into the Registration Form format
    form = RegistrationForm(request.form)
    
    # If sign up form is submitted via POST, validate the form
    if form.validate_on_submit():
        
        # Create the user and create a database entry
        user = User(form.name.data, form.email.data, form.password.data, 0, 0)
                    
        db.session.add(user)
        db.session.commit()
        
        flash('Thanks for registering', 'info')
        
        return redirect(url_for('.signin'))
    
    else:    
        return render_template('signup.html', form=form, 
            RECAPTCHA_PUB_KEY=environ.get("RECAPTCHA_PUB_KEY"))

# ---------------------------------------------------------------------------
# Sign Out Route: 
# ---------------------------------------------------------------------------            
@mod_auth.route("/signout/")

def signout():
    ''' Log out route '''
    
    if current_user.is_authenticated:
        logout_user()
        flash("You have been logged out", 'info')
        
    return redirect(url_for("base.index"))