# Import flask dependencies
from flask import Blueprint, render_template
                  
mod_base = Blueprint('base', __name__,
                    template_folder='templates',
                    static_folder='static')
                    
@mod_base.route('/')
def index():
    return render_template('./index.html')