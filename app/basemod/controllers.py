''' The business logic & routing controller of the base module

The is the controller aspect of the base module.
It is intentionally very bare bones

References:
    - The Parent Application
    - The Parent Application database
    - The Parent Application utilities
    - This module's: jinja templates

Yields:
    - Route: Index
    
Todo:
    - Overhaul expected in the near future - See the GitHub Projects
'''

# ---------------------------------------------------------------------------
# Imports:
# ---------------------------------------------------------------------------
from flask import Blueprint, render_template

# ---------------------------------------------------------------------------
# Methods, Decorators, and Vars: 
# ---------------------------------------------------------------------------
mod_base = Blueprint('base', 
                    __name__,
                    template_folder='templates',
                    static_folder='static')
                    
# ---------------------------------------------------------------------------
# Index Route:
# ---------------------------------------------------------------------------                   
@mod_base.route('/')
def index():
    ''' Renders the index page '''
    
    return render_template('./index.html')