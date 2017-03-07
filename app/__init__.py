'''
Desc.:      Initiation procedure for the application object
Purpose:    Creating and Configuring the app pre-run
Author:     Joel Tannas
Date:       MAR 03, 2017
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

# Define and Config
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
    ''' 404 Error Handler Function '''
    return render_template('404.html'), 404

# ---------------------------------------------------------------------------
# Define the database object (to be extended by modules and controllers)
# ---------------------------------------------------------------------------
db = SQLAlchemy(app)

# ---------------------------------------------------------------------------
# Import a module / component using its blueprint handler then register
# ---------------------------------------------------------------------------

# -- Import the website modules
from app.basemod.controllers import mod_base as base_module
from app.mod_auth.controllers import mod_auth as auth_module
#from app.mod_xyz.controllers import mod_xyz as xyz_module
# ..

# -- Register the website modules
app.register_blueprint(base_module)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

# ---------------------------------------------------------------------------
# Build the database using SQLAlchemy from registered blueprints
# ---------------------------------------------------------------------------
db.create_all()