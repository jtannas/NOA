'''
Desc.:      Form definitions using WTForms-Alchemy
Purpose:    ^
Author:     Joel Tannas
Date:       MAR 03, 2017
'''

# ---------------------------------------------------------------------------
# Generic Imports:
# ---------------------------------------------------------------------------

# Import Form and RecaptchaField
from flask_wtf import RecaptchaField

# Import Form elements
from wtforms import PasswordField, BooleanField, validators

# Import Form validators
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
        model = User
        only = ['password', 'email']
        unique_validator = None
                
class RegistrationForm(ModelForm):
    ''' User Registration Form '''
    
    class Meta:
        model = User
        only = ['name', 'email', 'password']
                
    confirm = PasswordField('Repeat Password',
                [Required(message='Must confirm a password'),
                EqualTo('password', message='Passwords must match')])
                
    accept_tos = BooleanField('I accept the Terms of Service', 
                [Required()])
                
    recaptcha = RecaptchaField()