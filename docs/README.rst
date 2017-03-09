====================
Documentation Guide
====================

The Upshot
==========
This project uses python docstrings to document all the python modules.
The preferred style is with Google Style python docstrings.
See here for examples: [Example Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
Do NOT use __{{property}}__ variables for version/author/etc... They are extra work, done better by GitHub, that are often outdated.

Technology in use
=================
Sphinx is a tool for generating documentation files from docstrings that are inside the code.
The docstrings must be written in RST format (a markup language).
There is an extension installed (sphinx-napoleon) that allows Google style docstrings.

[sphinx-apidocs](http://www.sphinx-doc.org/en/stable/man/sphinx-apidoc.html): Generates rst files for python modules in a given directory
[sphinx-autodoc](http://www.sphinx-doc.org/en/stable/ext/autodoc.html): Pulls docstrings from python modules into sphinx documentation
[sphinx](http://www.sphinx-doc.org/): Turns rst files into a variety of documentation formats
[sphinx-napoleon](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/): Allows the use of friendlier style docstrings

Setup Instructions
==================
MAKE THE DIRECTORY
-------------------
cd {{ projectroot }}  
sphinx-quickstart  
> Root path for the documentation [.]: ./documentation  
> Separate source and build directories (y/n) [n]: y  
> Name prefix for templates and static dir [_]:   
> Project name: NOA  
> Author name(s): Joel Tannas  
> Project version []: 0.0.1  
> Project release [0.0.1]:   
> Project language [en]:   
> Source file suffix [.rst]:   
> Name of your master document (without suffix) [index]:   
> Do you want to use the epub builder (y/n) [n]:  

> autodoc: automatically insert docstrings from modules (y/n) [n]: y  
> doctest: automatically test code snippets in doctest blocks (y/n) [n]:   
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y  
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y  
> coverage: checks for documentation coverage (y/n) [n]: y  
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]:   
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y  
> ifconfig: conditional inclusion of content based on config values (y/n) [n]: y  
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y  
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y  

> Create Makefile? (y/n) [y]: y  
> Create Windows command file? (y/n) [y]: y  

UPDATE THE CONF.PY IN DOCUMENTATION/SOURCE
-------------------------------------------
Add paths for sphinx to search for python modules (.py files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os  
import sys  
sys.path.insert(0, os.path.abspath('../..'))

Exclude certain patterns from those paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', './instance', './venv']


MAKE THE MODULE RST FILES
-------------------------
cd {{ projectroot }}/documentation  
sphinx-apidoc -o ./source ..

GENERATE THE DOCUMENTATION
--------------------------
cd {{ projectroot }}/documentation  
make clean  
make html

*There should now be a file {{ projectroot }}/documentation/build/html/index.html that gives the index of the project documentation*
