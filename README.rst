============
DRF_commands
============

DRF_commands is a Django package that helps you to create django rest framework endpoints faster using **manage.py**. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add Both "rest_framework" and "DRF_commands" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'DRF_commands',
    ]

2. Create a Django application using DRF_commands:

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




