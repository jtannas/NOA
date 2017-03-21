''' The business logic & routing controller of the legal module

The is the controller aspect of the module.

References:
    - This module's: jinja templates

Yields:
    - Route: Privacy, Displays the website privacy policy
    - Route: TOS, Displays the website Terms of Service
    
Todo:
    - Overhaul expected in the near future - See the GitHub Projects
'''

# ---------------------------------------------------------------------------
# Generic Imports: 
# ---------------------------------------------------------------------------
from os import environ
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# ---------------------------------------------------------------------------
# Application Imports: 
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Methods, Decorators, and Vars: 
# ---------------------------------------------------------------------------

# Define the blueprint for import into the parent application
mod_legal = Blueprint('legal', __name__, url_prefix='',
                    template_folder='templates',
                    static_folder='static')
                    
# ---------------------------------------------------------------------------
# Privacy Policy Route: 
# ---------------------------------------------------------------------------
@mod_legal.route('/privacy/')
def privacy():
    '''Displays the website privacy policy'''
    
    return render_template('./privacy.html')
    
# ---------------------------------------------------------------------------
# Terms of Service Route: 
# ---------------------------------------------------------------------------
@mod_legal.route('/TOS/')
def TOS():
    '''Displays the website terms of service'''
    
    return render_template('./TOS.html')