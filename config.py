'''
Desc.:      Configuration settings within the application object
Purpose:    app.config.from_object('config')
Author:     Joel Tannas
Date:       MAR 03, 2017
'''

# Define the application directory
import os
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
    CSRF_SESSION_KEY = os.environ.get("CSRF_SESSION_KEY")  # !!! SECRET !!!
    if not CSRF_SESSION_KEY:
        raise RuntimeError("CSRF_SESSION_KEY not set")
          
     # Secret key for signing cookies
    SECRET_KEY = os.environ.get("SECRET_KEY") # !!! SECRET !!!
    if not SECRET_KEY:
        raise RuntimeError("SECRET_KEY not set")
     
    # Recaptcha keys
    RECAPTCHA_USE_SSL = True
    RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY") # !!! SECRET !!!
    if not RECAPTCHA_PUBLIC_KEY:
        raise RuntimeError("RECAPTCHA_PUBLIC_KEY not set")
    if not RECAPTCHA_PRIVATE_KEY:
        raise RuntimeError("RECAPTCHA_PRIVATE_KEY not set")
          
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