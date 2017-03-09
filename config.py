''' Configuration settings for the Flask application.

This module provides the configuration settings for the flask application.
Since not every setting (i.e. development, testing, production) uses the same
settings, multiple configurations are supported.

Using Configurations
--------------------
1. A 'Base' configuration class is created with default settings
2. More specific configuration classes then inherit the base class
3. Changes can be made to individual configurations within their class definitions
4. The configurations are collected into a dict
5. Within your applications __init__.py, call the following code:
    ''app.config.from_object(config['{{dict key}}'])''
    
Database Note
-------------
The location of the database for the app is set within this file.
As a default, it is called via SQLite and set within the same directory as the
config file.

Customizing for your application
--------------------------------
Todo:
    * Support configuration from an Instance Folder for individual deployments
'''

# Define the application directory
import os
import warnings
from tempfile import gettempdir
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    ''' 
    Base configuration for the application.
    
    This configuration is meant as a 'baseline' set of configuration setting that
    is then extended via more specific configuration. It does not inherit anything.
    '''
    
    # Set the Application Name
    APP_NAME = "NOA"

    # Set to Debug Mode
    DEBUG = True
     
    # Use server side sessions for greater security
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
    '''Dev configuration
    
    Flask App Dev configuration, inherits the BaseConfig and modifies it.
    The database is set to a generic app.db for development
        * 
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    DEBUG = True
    
class TestConfig(BaseConfig):
    '''Testing configuration
    
    Flask App Test configuration, inherits the BaseConfig and modifies it.
    Is intended to use a duplicate of the production database to allow testing
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'NOA.1.db')
    DEBUG = False

class ProdConfig(BaseConfig):
    '''Production configuration
    
    Flask App Productin configuration, inherits the BaseConfig and modifies it.
    '''
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'NOA.db')
    
    

config = {
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig,
    "default": DevConfig
}