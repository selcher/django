
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

Add super user:
> python manage.py createsuperuser --settings=config.settings.local

Project:
> blogprog_project ( abandon )
    - weblog

> shootingstar_project
    - blog ( idea, wish, dream )

Runserver:
> cd shootingstar_project
> python manage.py runserver --settings=config.settings.local

Model Update:
> python manage.py makemigrations --settings=config.settings.local
> python manage.py migrate --settings=config.settings.local

PostgreSQL:
> psql -U <user_name>
> password: <password>
> CREATE USER <user_name>
> CREATE DATABASE shootingstar OWNER <user_name>

Pull git updates:
> git pull
> python manage.py collectstatic --settings=config.settings.local
