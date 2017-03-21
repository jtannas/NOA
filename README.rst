.. _README:
====================================
NOA: Nameless Organizing Application
====================================
This is a Flask web application whose main purposes are:
    - serve as a template for future Flask development work on large websites (via adding modules)
    - act as a Team To-Do list

Since it is meant as a template using best practices, I will refactoring it fairly often during active development as my skills improve.

.. contents:: 

General Information
-------------------
Inspiration and Guide
~~~~~~~~~~~~~~~~~~~~~
I began with Flask while doing the CS50X course run by David J Malan of Harvard.
A lot of the basics of the application are coming from http://exploreflask.com/en/latest/

The reason it's a team organizer (even though that's been done many times already) is that I'm drawing from memories of something I built in MS Access at a previous job. Learning all the technology is enough to occupy my brain without having to be creative too.



General Structure
~~~~~~~~~~~~~~~~~
This flask application is built around Flask blueprints. They makes it easy to seperate different functions into self-contained modules. I'm heavily emphasizing modular code in this project so that I get a better understanding of how to build a larger project from independent chunks.

The 'app' folder is the actual application, and is initialized via the ./app/__init__.py file, and pulls configuration information from the config.py file. There are also folders (that have been .gitignore'd) for /instance and /env. The instance folder is for instance specific information (e.g. keys) and the env folder is for the virtual environment information. If possible on your computer, I recommend virtualenvwrapper to keep your virtual environments out of the application folder.

Useful Links
    - http://exploreflask.com/en/latest/index.html
    - https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
    - http://flask.pocoo.org/docs/0.12/blueprints/

Technologies
------------
Documentation
~~~~~~~~~~~~~
Documentation is done via python docstrings in the Google format. These are then collected into the documention by a program called Sphinx (with the help of some extensions). :ref:`See the Documentation ReadMe for more details<DocumenationREADME>`.

Databases
~~~~~~~~~
For database interaction, I am using Flask_SQLAlchemy. This lets you interact with the databases in a much more 'pythonic' way.
It also takes care of guarding against SQL injection, so the app is structurally protected against it.
If the database file does not exist, SQLAlchemy will create it based off the table definitions within the file.

Forms
~~~~~
WTForms is the starting point for creating forms.
This is then extended via WTForms_Alchemy. This lets you populate forms directly from SQLAlchemy tabledefinions (including built in validation).

Useful Links
    - http://flask.pocoo.org/docs/0.12/patterns/wtforms/
    - http://wtforms.readthedocs.io/en/latest/#
    - https://wtforms-alchemy.readthedocs.io/en/latest/

Todo:
- Add tech for in browser validation using Javascript (+?)

Templates
~~~~~~~~~
I am using the Jinja2 templating engine to fill the content of the html pages, while relying mostly on Bootstrap for the responsive design. Flask-JSGlue is also used to bring python commands into the javascript.

Testing
~~~~~~~
Todo:
- Implement pytest
