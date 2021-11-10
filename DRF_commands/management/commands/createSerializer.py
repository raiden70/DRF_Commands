from django.core.management.base import BaseCommand
from django.conf import settings
from pathlib import Path

import os
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("AppName",type=str)
        parser.add_argument("SerializerName",type=str)

    def handle(self, *args, **options):
        BASE_DIR = settings.BASE_DIR
        CURRENT_DIR=Path(__file__).resolve().parent

        if (not os.path.isfile(str(BASE_DIR / options['AppName']) + "/serializers/" + options['SerializerName'].capitalize() + '.py')):
            skull = open(CURRENT_DIR/"serializer.txt", "r")
            with open(str(BASE_DIR / options['AppName']) + "/serializers/" + options['SerializerName'].capitalize() + '.py', 'w') as f:
                s = skull.read().replace("{{className}}", options['SerializerName'].capitalize())
                f.write(s)
                f.close()
            with open(str(BASE_DIR / options['AppName']) + "/serializers/__init__.py", 'a+') as f:
                f.write("from ." + options['SerializerName'].capitalize() + " import " + options['SerializerName'].capitalize() + "Serial" + "\n")
                f.close()
        else:
            print("The file " + options['SerializerName'].capitalize() + ".py already exists !")
