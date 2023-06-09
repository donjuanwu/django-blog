#!/usr/bin/env python
import os
import sys

"""
Assignment: 07
Date: 5/15/23
File name: manage.py
Purpose:
- a management control script
- Django's command-line utility for administrative tasks

How it works:
The `django-admin` command that we used to create the project has sub-commands that allow you to:
- creating a new project or app
- running the development server
- executing tests
- entering a python interpreter
- entering a database shell session with your database
- much much more (run django-admin without an argument)

The `manage.py` script wraps this functionality in the context of your project: it communicates your project settings 
to `django-admin`.

The environment variable DJANGO_SETTINGS_MODULE is how the manage.py script knows about your project’s environment. 
Specifically, it knows that our project is named mysite. This is why you shouldn’t rename the mysite project package.

Date        Developer           Activities
5/18/23     Don D.              Run python manage.py runserver
                                Unable to log into 127.0.0.1:8000/admin
                                Need to recreate superuser on pycharm terminal
                                > python manage.py createsuperuser
                                name: doncd
                                pw: leyla2004
"""


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
