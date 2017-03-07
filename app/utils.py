'''
Desc.:      Non-module specific classes and methods 
Purpose:    Useful utilities to make like easier when coding other modules
Author:     Joel Tannas
Date:       MAR 07, 2017
'''

from . import db
from flask import request, session
from flask_wtf import Form
from urllib.parse import urlparse, urljoin
from wtforms_alchemy import model_form_factory

# ---------------------------------------------------------------------------
# Define a method for checking the safety of redirects
# ---------------------------------------------------------------------------
def is_safe_url(target):
    ''' Check to see if a URL redirects within the website
    by http://flask.pocoo.org/snippets/62/
    '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


# ---------------------------------------------------------------------------
# Build a model form that integrates WTForms_Alchemy with Flask_wtf
# ---------------------------------------------------------------------------
# http://wtforms-alchemy.readthedocs.io/en/latest/advanced.html#using-wtforms-alchemy-with-flask-wtf
BaseModelForm = model_form_factory(Form)

class ModelForm(BaseModelForm):
    ''' Base model WTForm to build others off of'''
    @classmethod
    def get_session(self):
        return db.session

# ---------------------------------------------------------------------------
# Build a model tabledef for the rest of the database table to inherit
# ---------------------------------------------------------------------------
class ModelTable(db.Model):
    ''' Base model tabledef to build others off of '''

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())
