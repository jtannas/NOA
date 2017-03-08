'''
Desc.:      Configuration settings within the application object
Purpose:    app.config.from_object('config')
Author:     Joel Tannas
Date:       MAR 03, 2017
'''

# Define the application directory
import os
import warnings
BASE_DIR = os.path.abspath(os.path.dirname(__file__))       

class BaseConfig:
    ''' 
    Base configuration for the application.
    It is meant as a 'baseline' set of configuration setting that
    is then extended via more specific configuration
    '''
    APP_NAME = "NOA"

    # Set to Debug Mode
    DEBUG = True
     
    # Use server side sessions for greater security
    from tempfile import gettempdir
    SESSION_FILE_DIR = gettempdir()
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"
     
    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}
     
    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2
     
    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED     = True
    CSRF_SESSION_KEY = os.environ.get("CSRF_SESSION_KEY")
    if not CSRF_SESSION_KEY:
        warnings.warn("CSRF_SESSION_KEY not set", RuntimeWarning)
        CSRF_SESSION_KEY = 'ChangeMe'
          
     # Secret key for signing cookies
    SECRET_KEY = os.environ.get("SECRET_KEY")  or 'ChangeMe'
    if not SECRET_KEY:
        warnings.warn("SECRET_KEY not set", RuntimeWarning)
        SECRET_KEY = 'ChangeMe'
     
    # Recaptcha keys
    RECAPTCHA_USE_SSL = True
    RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
    if not RECAPTCHA_PUBLIC_KEY:
        warnings.warn("RECAPTCHA_PUBLIC_KEY not set", RuntimeWarning)
        RECAPTCHA_PUBLIC_KEY = 'ChangeMe'
    if not RECAPTCHA_PRIVATE_KEY:
        warnings.warn("RECAPTCHA_PRIVATE_KEY not set", RuntimeWarning)
        RECAPTCHA_PRIVATE_KEY = 'ChangeMe'
          
class DevConfig(BaseConfig):
    '''Dev config'''
    # TODO
    
class TestConfig(BaseConfig):
    '''Testing config'''
    # TODO

class ProdConfig(BaseConfig):
    '''Production config'''
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'NOA.db')
    
    

config = {
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig,
    "default": DevConfig
}