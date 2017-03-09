''' The Flask Application __init__ file

This file initiates and configures the flask application.
Ideally, it contains only configurations and objects that are relevant to 
the entire application (eg. HTTP error handling).

The reason behind this minimalism is that this flask application uses a
modular structrure based on blueprints.

Note:
    See [Flask's explanation](http://flask.pocoo.org/docs/0.12/blueprints/) for
    details.

The benefit of this is that websites can be extended by dropping in new code
modules, with the only application level work being registering them within
this file.

Yields:
    - Configures the application
    - Defines the db (database object) using SQLAlchemy
    - Prevents caching in debug mode
    - Converts all pages to https (when out of debug mode)
    - Protects against Cross Site Request Forgery (CSRF)
    - Sets the error handling methods for HTTP errors
    - Registers application blueprints to extend the application 
    - Creates the database tables (if needed) (depends on blueprint models)

Todo:
    * Add in configuration from an instance folder
'''

# ---------------------------------------------------------------------------
# Import flask and template operators
# ---------------------------------------------------------------------------
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_sslify import SSLify
from flask_wtf import CSRFProtect
from flask_wtf.csrf import CSRFError

# ---------------------------------------------------------------------------
# Define & Configure the WSGI application object
# ---------------------------------------------------------------------------
app = Flask(__name__)
from config import *
app.config.from_object(config['dev'])

# if in debug, do not cache webpages so that changes are shown on refresh
if app.config["DEBUG"]:
    
    toolbar = DebugToolbarExtension(app)
    
    @app.after_request
    def after_request(response):
        ''' Modifies the response header to prevent caching'''
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response
        
# ---------------------------------------------------------------------------
# Define the database object (to be extended by modules and controllers)
# ---------------------------------------------------------------------------
db = SQLAlchemy(app)

# ---------------------------------------------------------------------------
# SSLify the application for https (only valid when app.debug = false)
# ---------------------------------------------------------------------------
sslify = SSLify(app)

# ---------------------------------------------------------------------------
# Globally protect against Cross-Site Request Forgery (CSRF)
# ---------------------------------------------------------------------------
csrf = CSRFProtect(app)

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    ''' Handle Cross Site Scripting Errors '''
    
    return render_template('csrf_error.html', reason=e.description), 400

# ---------------------------------------------------------------------------
# HTTP error handling
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def not_found(error):
    ''' 404 HTTP Error Handler Function 
    
    Handles 404 HTTP Errors.
    Renders a 404 template page.'''
    
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    ''' 500 HTTP Internal Server Error Handler Function 
    
    Handles 500 HTTP Internal Server Error Function
    Rolls back any (possibly erroneous) uncommitted database session changes,
    then renders the 500 template page.'''
    
    db.session.rollback()
    return render_template('500.html'), 500

# ---------------------------------------------------------------------------
# Import a module / component using its blueprint handler then register
# ---------------------------------------------------------------------------

# -- Import the website modules
from app.basemod.controllers import mod_base as base_module
from app.mod_auth.controllers import mod_auth as auth_module
#from app.mod_xyz.controllers import mod_xyz as xyz_module
# ...

# -- Register the website modules
app.register_blueprint(base_module)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ...

# ---------------------------------------------------------------------------
# Build the database using SQLAlchemy from registered blueprints
# ---------------------------------------------------------------------------
db.create_all()