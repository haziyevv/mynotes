# DJANGO

1. To start a project named mysite:

```
django-admin startproject mysite
```

2. These files will be created when the project is created:

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

**manage.py** --> lets you interact with this django project.

inner **mysite** directory is the actual Python package for the project.

**settings.py** --> all the settings and configurations for this Django project.

**urls.py** --> url declarations for the Django project. A **table of contents** for the site. 

**asgi.py** --> An entry point for ASGI-compatible web servers.

**wsgi.py** --> An entry point for WSGI-compatible web servers.

3. **django-admin** --> django's command line utility for administrative tasks. 

4. python3 manage.py runserver --> will run the project in browser.

5. **python3 manage.py startapp polls** --> will create an app named polls.

6. 

### How DJANGO processes a request ?

1. Django determines the root **URLconf** module to use. This is the value of the **ROOT\_URLCONF** setting in the **settings.py**. But if the incoming **HTTPRequest** object has a **urlfconf** attribute, its value wil be used in place of the **ROOT\_URLCONF** setting.

2. Django loads that Python module and looks for the variable **urlpatterns**. 


