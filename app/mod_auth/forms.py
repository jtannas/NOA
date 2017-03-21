''' Form definitions using WTForms-Alchemy

This module contains the userform definitions for how users interract with
application data. They are created using WTForms, and are then passed to the
Jinja templates by the module controller.

WTForms-Alchemy is an extension that allows WTForms to be generated from 
SQLAlchemy models. This ensures that the validation is synched between the 
two (though overrides are possible).

References:
    - This module's: User model
    - The Parent Application ModelForm
    
Yields:
    - Login Form
    - Registration Form
'''

# ---------------------------------------------------------------------------
# Generic Imports:
# ---------------------------------------------------------------------------
from flask_wtf import RecaptchaField
from wtforms import PasswordField, BooleanField, validators
from wtforms.validators import Required, EqualTo, Regexp

# ---------------------------------------------------------------------------
# App Imports:
# ---------------------------------------------------------------------------
from .models import User
from ..utils import ModelForm

# ---------------------------------------------------------------------------
# Form Definitions:
# ---------------------------------------------------------------------------
class LoginForm(ModelForm):
    ''' User Login Form '''
    
    class Meta:
        ''' Pull the User SQLAlchemy definition as a base for the form '''
        
        model = User
        only = ['password', 'email']
        unique_validator = None
                
class RegistrationForm(ModelForm):
    ''' User Registration Form '''
    
    class Meta:
        ''' Pull the User SQLAlchemy definition as a base for the form '''
        model = User
        only = ['name', 'email', 'password']
    
    #: Password Confirmation Field            
    confirm = PasswordField('Repeat Password',
                [Required(message='Must confirm a password'),
                EqualTo('password', message='Passwords must match')])
    
    #: Terms of Service Acceptance            
    accept_tos = BooleanField('I accept the Terms of Service', 
                [Required()])
    
    #: Recaptcha to prevent bot registration            
    recaptcha = RecaptchaField()