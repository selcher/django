
// Two Scoops of Django 1.8 ( example )

Create virtualenv
> mkvirtualenv blogprog
> workon blogprog
> deactivate

Generate boilerplate project template
( use bash / mingw32 for windows, terminal will lose git on virtualenv )
> cookiecutter https://github.com/pydanny/cookiecutter-django.git


Create project:
> django-admin.py startproject blogprog
> cd blogprog

Create app:
> django-admin.py startapp weblog


Project:
> blogprog_project ( abandon )
    - weblog

> shootingstar_project
    - blog ( idea, wish, dream )

Runserver:
> cd shootingstar_project
> python manage.py runserver --settings=config.settings.local
