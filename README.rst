===
NOA
===
Nameless Organizing Application
-------------------------------
This is a Flask web application whose main purposes are:
- act as a Team To-Do list
- serve as a template for future Flask development work on large websites (via adding modules)
 
General Information
-------------------
Inspiration and Guide
~~~~~~~~~~~~~~~~~~~~~
I began with Flask while doing the CS50X course run by David J Malan of Harvard.
A lot of the basics of the application are coming from http://exploreflask.com/en/latest/

General Structure
~~~~~~~~~~~~~~~~~
This flask application is built around Flask blueprints. This makes it easy to seperate different functions into self-contained modules.
The 'app' folder is the actual application, and is initialized via the ./app/__init__.py file, and pulls configuration information from the ./config.py file.

There are also folders (that have been .gitignore'd) for /instance and /env.
The instance folder is for instance specific information (e.g. keys) and the env folder is for the virtual environment information.
If possible on your computer, I recommend virtualenvwrapper to keep your virtual environments out of the application folder.

> ##### Useful Links
> - http://exploreflask.com/en/latest/index.html
> - https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
> - http://flask.pocoo.org/docs/0.12/blueprints/

Templates
~~~~~~~~~
I am using the Jinja2 templating engine to create the html templates. Flask-JSGlue is also used to bring python commands into the javascript.

Databases
~~~~~~~~~
For database interaction, I am using Flask_SQLAlchemy. This lets you interact with the databases in a much more 'pythonic' way.
It also takes care of guarding against SQL injection, so the app is structurally protected against it.
If the database file does not exist, SQLAlchemy will create it based off the table definitions within the file.

Forms
~~~~~
WTForms is the starting point for creating forms.
This is then extended via WTForms_Alchemy. This lets you populate forms directly from SQLAlchemy tabledefinions (including built in validation).

> * Useful Links *
> - http://flask.pocoo.org/docs/0.12/patterns/wtforms/
> - http://wtforms.readthedocs.io/en/latest/#
> - https://wtforms-alchemy.readthedocs.io/en/latest/

WIP NOTES
=========
Notes to self for future work not specific to any modules

Flask WTForms AJAX
    https://github.com/saltycrane/flask-jquery-ajax-example
    http://flask-wtf.readthedocs.io/en/latest/csrf.html#ajax
    
Sphinx Documentation with Docstrings
    http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html