# Base Module Readme

## What is this?
This is the 'base' front end module of the application.
The templates and static files serve as the base layout for the rest of the application.
It is set up like this so that the root directory of the application contains only modules.
Different layouts can be swapped in by swapping different layout files.

## Concept
macros.html -> layout.html -> template.html -> index & 404 pages

The macros html contains jinja2 macros.
The layout html is the general layout of the pages with *no site specific information*.
The template page contains all the site specific information to load into the layout.
The index and 404 pages are there because it doesn't make sense to put them into an auxilary module.