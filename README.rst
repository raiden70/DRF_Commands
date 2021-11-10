============
DRF_commands
============

DRF\_commands is a Django package that helps you to create django rest
framework endpoints faster using **manage.py**.

You can visit **Django rest framework** website for more information
about generic views:https://www.django-rest-framework.org/

Quick start
-----------

1. Run ``pip install DRF_commands``
2. Add Both "rest_framework" and "DRF_commands" to your
   **INSTALLED_APPS** of your **settings.py** like this::

           INSTALLED_APPS = [
               ...
               'rest_framework',
               'DRF_commands',
           ]

3. Create a Django application using DRF_commands:

``python manage.py createApp [yourAppName]``

3. Run ``python manage.py`` using custom commands of DRF_commands to create generic views.

Available commands:
-------------------
- createApp [yourAppName]
- createSerializer [appName][serializerName]
- APIView [appName][viewName]
- CreateAPIView [appName][viewName]
- DestroyAPIView [appName][viewName]
- ListAPIView [appName][viewName]
- ListCreateAPIView [appName][viewName]
- RetrieveAPIView [appName][viewName]
- RetrieveDestroyAPIView [appName][viewName]
- RetrieveUpdateAPIView [appName][viewName]
- RetrieveUpdateDestroyAPIView [appName][viewName]
- UpdateAPIView [appName][viewName]

Generated application working tree:
-----------------------------------

::

    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models
    │   └── __init__.py
    ├── serializers
    │   └── __init__.py
    ├── static
    │   └── myapp
    ├── templates
    │   └── myapp
    ├── tests.py
    ├── urls.py
    └── views
        └── __init__.py




