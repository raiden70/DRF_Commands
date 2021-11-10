from django.core.management.base import BaseCommand
import os
from pathlib import Path
from django.conf import settings

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("AppName",type=str)

    def handle(self, *args, **options):
        #initializing directories
        os.mkdir(options['AppName'])
        os.mkdir(options['AppName']+"/migrations")
        os.mkdir(options['AppName']+"/models")
        os.mkdir(options['AppName']+"/serializers")
        os.mkdir(options['AppName']+"/views")
        os.mkdir(options['AppName']+"/templates")
        os.mkdir(options['AppName']+"/static")
        os.mkdir(options['AppName']+"/templates/"+options['AppName'])
        os.mkdir(options['AppName']+"/static/"+options['AppName'])
        #creating files
        open(options['AppName']+"/migrations/__init__.py","x")
        open(options['AppName']+"/models/__init__.py","x")
        open(options['AppName']+"/serializers/__init__.py","x")
        open(options['AppName']+"/views/__init__.py","x")
        open(options['AppName']+"/__init__.py","x")
        #fill files
        urls=open(options['AppName']+"/urls.py","w")
        apps=open(options['AppName']+"/apps.py","w")
        tests=open(options['AppName']+"/tests.py","w")
        admin=open(options['AppName']+"/admin.py","w")
        CURRENT_DIR=Path(__file__).resolve().parent

        #apps part
        apps_content=open(CURRENT_DIR/"apps.py.txt","r")
        apps.write(apps_content.read().replace("[[AppName]]",options['AppName']))
        apps.close()
        #URL part
        url_content=open(CURRENT_DIR/"urls.py.txt",'r')
        urls.write(url_content.read().replace("[[AppName]]",options['AppName']))
        urls.close()
        #Admin part
        admin.write("from django.contrib import admin \n\n # Register after imporing your models here. \n #admin.site.register('modelName')")
        admin.close()
        #test part
        tests.write("from django.test import TestCase \n\n # Create your tests here. ")
        tests.close()
        #adding the url of the application in project urls.py
        PROJECT_NAME = os.path.basename(settings.BASE_DIR)
        with open(str(settings.BASE_DIR)+"/"+PROJECT_NAME+"/urls.py","r") as f:
            include_string="from django.urls import path,include"
            data=f.read()
            if(not include_string in data):
                data=data.replace("from django.urls import path",include_string)
            f.close()
        with open(str(settings.BASE_DIR)+"/"+PROJECT_NAME+"/urls.py","w") as f:
            f.write(data)
            f.close()
        with open(str(settings.BASE_DIR)+"/"+PROJECT_NAME+"/urls.py","a+") as f:
            p = "\nurlpatterns+=[path('" + options['AppName'] + "/',include('" + options['AppName']+".urls'))]"
            f.write(p)
            f.close()

