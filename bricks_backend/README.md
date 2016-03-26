# Heroku Django Starter Template

An utterly fantastic project starter template for Django 1.9.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku
    $ If this is a new heroku app:
    - Create the app on heroku
    - Connect the app with a branch on github
    - Deploy manually from heroku a first time (next times deployment will be launch automatically)
    - Then you need to init the db and create admin account:
    `heroku --app [APP_NAME] run bash` to connect to your app heroku server
    `./manage.py migrate` it will initialize the db
    `./manage.py createsuperuser` to create an admin account
    `./manage.py shell`
    `from django.contrib.sites.models import Site`
    `s = Site.objects.get()``
    `s.domain = [HEROKU_DOMAIN_URL]` where [HEROKU_DOMAIN_URL] is the domain you get from heroku acces page
    `s.save`

    
See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
